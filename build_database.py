import os
import json
import subprocess
import re

database = {
    "desktop_apps": {},
    "store_apps": {},
    "files": {},
    "folders": {}
}

START_MENU_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(
        r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
    )
]

for start_path in START_MENU_PATHS:

    for root, dirs, files in os.walk(start_path):

        for file in files:

            if file.endswith(".lnk"):

                app_name = (
                    file
                    .replace(".lnk", "")
                    .lower()
                )

                path = os.path.join(
                    root,
                    file
                )

                database[
                    "desktop_apps"
                ][app_name] = path

with open(
    "cosmio_database.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        database,
        f,
        indent=4
    )

print(
    f"Saved "
    f"{len(database['desktop_apps'])} "
    f"desktop apps."
)

def get_store_apps():

    apps = {}

    try:

        result = subprocess.run(
            [
                "powershell",
                "-Command",
                "Get-StartApps"
            ],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        lines = result.stdout.splitlines()

        for line in lines:

            if "!" in line:

                parts = re.split(r"\s{2,}", line.strip())

                if len(parts) >= 2:

                    name = parts[0].lower()

                    appid = parts[-1]

                    apps[name] = appid

    except Exception as e:

        print("STORE APP ERROR:", e)

    return apps
database["store_apps"] = get_store_apps()