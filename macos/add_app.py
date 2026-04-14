#!/usr/bin/env python3
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APPS_JSON_PATH = os.path.join(SCRIPT_DIR, "protocol_handler/apps.json")
DASHBOARD_HTML_PATH = os.path.join(SCRIPT_DIR, "dashboard/dashboard.html")


def main():
    print("Add a new app to the Ack! App Launcher\n")

    app_key = input("Enter app key (e.g., myapp): ").strip()
    if not app_key:
        print("App key cannot be empty.")
        return

    app_name = input("Enter app name (e.g., My App): ").strip()
    icon_url = input("Enter icon URL or path: ").strip()
    command = input("Enter command to run: ").strip()

    print(f"\nAdding app '{app_key}'...")

    # Update apps.json
    try:
        with open(APPS_JSON_PATH, "r") as f:
            apps_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {APPS_JSON_PATH} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not parse {APPS_JSON_PATH}.")
        return

    if app_key in apps_data:
        print(f"Warning: App key '{app_key}' already exists in apps.json. Overwriting.")

    apps_data[app_key] = {"cmd": command}

    with open(APPS_JSON_PATH, "w") as f:
        json.dump(apps_data, f, indent=2)
        f.write("\n")
    print(f"Updated {APPS_JSON_PATH}")

    # Update dashboard.html
    try:
        with open(DASHBOARD_HTML_PATH, "r") as f:
            dashboard_html = f.read()
    except FileNotFoundError:
        print(f"Error: {DASHBOARD_HTML_PATH} not found.")
        return

    placeholder = "/* *** add new app placeholder *** */"
    if placeholder not in dashboard_html:
        print(f"Error: Placeholder '{placeholder}' not found in {DASHBOARD_HTML_PATH}.")
        return

    new_app_entry = f"""{app_key}: {{
          cover_art: '{icon_url}',
          name: '{app_name}',
        }},
        {placeholder}"""

    dashboard_html = dashboard_html.replace(placeholder, new_app_entry, 1)

    with open(DASHBOARD_HTML_PATH, "w") as f:
        f.write(dashboard_html)
    print(f"Updated {DASHBOARD_HTML_PATH}")
    print("Done!")


if __name__ == "__main__":
    main()
