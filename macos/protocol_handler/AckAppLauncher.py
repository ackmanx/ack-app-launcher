import json
import os
import subprocess
import sys

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "apps.json")


def notify(title, message):
    """Sends a native macOS notification."""
    # We use osascript to trigger the notification center
    apple_script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", apple_script])


def main():
    if not os.path.exists(CONFIG_PATH):
        notify("Ack Launcher Error", "Configuration file (apps.json) not found.")
        exit(1)

    if len(sys.argv) < 2:
        return

    # Parse the app key (e.g., "ack-app-launch://spotify" -> "spotify")
    raw_url = sys.argv[1]
    app_key = raw_url.replace("ack-app-launch://", "").rstrip("/")

    with open(CONFIG_PATH, "r") as file:
        apps = json.load(file)

    if app_key in apps:
        app_config = apps[app_key]
        cmd = app_config["cmd"]

        # shell=True is required here to parse the full command string
        subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    else:
        notify("Ack! App Launcher", f"App '{app_key}' not found in apps.json.")
        print(f"{app_key} not found in config")


if __name__ == "__main__":
    main()
