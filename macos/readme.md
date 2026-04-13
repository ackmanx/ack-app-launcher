# MacOS Tahoe Usage

## Architecture

The shim is essentially the handler for the `ack-app-launch://` custom protocol.

Our protocol handler simply fowards the message it receives to our Python script that actually does the logic and opening.

## If updating the dashboard, Python script or apps JSON file

The dashboard can be edited in any way and live anywhere because all it does is use links that are globally registered.

The Python script or apps file can be edited from within the app package and changes will be effectively immediately because there's no compilation step for them.

## If updating the metadata and Apple stuff, you need to recompile things

Such as app icon, AppleScript shell, protocol structure...

### Clean out old app

```bash
rm -rf /Applications/AckLauncher.app
```

### Compile the shim

This will create a new `.app` and other junk I don't understand. It puts it in `/Applications` automatically due to our using `-o` flag.

The shim is essentially the handler for the `ack-app-launch://` custom protocol.

```bash
osacompile -o /Applications/AckLauncher.app shim.applescript
```

### Copy non-Apple assets into the app package

```bash
cp protocol_handler/AckAppLauncher.py /Applications/AckLauncher.app/Contents/Resources/
cp protocol_handler/apps.json /Applications/AckLauncher.app/Contents/Resources/
```

### Apply protocol configuration and some extras

```bash
PLIST="/Applications/AckLauncher.app/Contents/Info.plist"

# Add the protocol
plutil -insert CFBundleURLTypes -json '[{"CFBundleURLSchemes":["ack-app-launch"],"CFBundleURLName":"Ack App Launcher"}]' "$PLIST"

# Hide the Dock icon (UIElement mode)
plutil -replace LSUIElement -string "1" "$PLIST"

# Clear the quarantine flag for the new build
xattr -rd com.apple.quarantine /Applications/AckLauncher.app

# Refresh Launch Services one last time
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -f /Applications/AckLauncher.app
```
