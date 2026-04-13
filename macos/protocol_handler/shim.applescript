on open location theURL
    set scriptPath to (POSIX path of (path to me)) & "Contents/Resources/AckAppLauncher.py"
    do shell script "/usr/bin/python3 " & quoted form of scriptPath & " " & quoted form of theURL
end open location
