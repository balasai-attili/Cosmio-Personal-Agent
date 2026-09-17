import os

START_MENU_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(
        r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
    )
]

with open(
    "apps.txt",
    "w",
    encoding="utf-8"
) as f:

    for start_path in START_MENU_PATHS:

        for root, dirs, files in os.walk(start_path):

            for file in files:

                if file.endswith(".lnk"):

                    f.write(
                        file.replace(
                            ".lnk",
                            ""
                        ) + "\n"
                    )

print("Done")