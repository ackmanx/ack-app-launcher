# Ack! App Launcher

This is a minimalist dashboard for launching any app. It works by using links in the dashboard that point to a custom protocol `ack-app-launcher://`. Upon click, this invokes a tiny Python script that then will execute the command to open the given application.

## First-time Setup

Install Python. For Windows 11, I just opened up a shell and typed `python` and was prompted to install it.

Afterwards, I used one of the two to find where it was installed:

- CMD: `where python`
- PowerShell: `Get-Command python`

Edit `Register_Custom_Protocol.reg` for two things:

- Tell Windows what program to run upon clicking on our custom protocol
  - The `[HKEY_CLASSES_ROOT\ack-app-launch\shell\open\command]` section
  - The entire command says to run python and then passes the AckAppLauncher script to python to run
  - Update the path for where Python is, making sure to escape
- Tell Python where our script is
  - Update the path to where `AckAppLauncher.py` is located. Be sure that wherever it is, `apps.json` is with it

## Adding Apps

To add an app to the dashboard, there's two places to edit

- `Dashboard.html`:
  - The `window.apps` object stores the apps the dashboard will show
  - The app name key is what will be sent to the protocol handler. Everything else is for visuals
  - If `cover_art` is provided, that will be used. Otherwise it will use `steam_id_for_cover` to generate the cover art URL from Steam
- `apps.json`:
  - The app name key here has to match what you used in the dashboard
  - Provide the command to run

## Testing

The launcher and your `app.json` can be tested manually

Windows:
python AckAppLauncher.py ack-app-launch://fallout_new_vegas_vnv

Mac:
python3 AckAppLauncher.py ack-app-launch://fallout_new_vegas_vnv
