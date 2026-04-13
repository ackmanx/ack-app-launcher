import json
import os
import subprocess
import sys

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "apps.json")


if not os.path.exists(CONFIG_PATH):
    exit(1)


# All this script does is look up the requested app in the config store, then open it
def main():
    if len(sys.argv) < 2:
        return

    # Parse the app key (e.g., "ack-app-launch://fallout/" -> "fallout")
    raw_url = sys.argv[1]
    app_name = raw_url.replace("ack-app-launch://", "").rstrip("/")

    with open(CONFIG_PATH, "r") as file:
        apps = json.load(file)

    if app_name in apps:
        app_config = apps[app_name]
        cmd = app_config["cmd"]

        print(f"Found {app_name}, executing: {cmd}")

        # Using shell=True allows you to pass the full string
        # like "open -a Spotify" or "open steam://..."
        subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    else:
        print(f"{app_name} not found in config")


if __name__ == "__main__":
    main()
