import os
import json

START_MENU_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(
        r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
    )
]

apps = {}

for start_path in START_MENU_PATHS:

    for root, dirs, files in os.walk(start_path):

        for file in files:

            if file.endswith(".lnk"):

                name = file.replace(
                    ".lnk",
                    ""
                ).lower()

                path = os.path.join(
                    root,
                    file
                )

                apps[name] = path

with open(
    "apps.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        apps,
        f,
        indent=4
    )

print(
    f"Saved {len(apps)} apps."
)