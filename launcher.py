import json
import os
import subprocess

# Load app database

with open(
    "cosmio_database.json",
    "r",
    encoding="utf-8"
) as f:

    DATABASE = json.load(f)

APPS = DATABASE["apps"]
# Common aliases

ALIASES = {
    "chrome": "google chrome",
    "powershell": "windows powershell",
    "vs code": "visual studio code",
    "vscode": "visual studio code",
    "opera": "opera gx browser",
    "cmd": "command prompt",
    "telegram": "telegram",
    "discord": "discord",
    "valorant": "valorant",
    "genshin": "genshin impact"
}


def find_app(app_name):

    app_name = app_name.lower().strip()

    # Apply aliases

    if app_name in ALIASES:
        app_name = ALIASES[app_name]

    # Exact match first

    if app_name in APPS:
        return APPS[app_name]

    # Partial match

    for name, path in APPS.items():

        if (
            app_name in name
            or
            name in app_name
        ):

            return path

    return None


def open_app(app_name):

    app = find_app(app_name)

    if not app:
        return False

    try:

        appid = app["appid"]

        print("APPID:", appid)

        subprocess.Popen(
        [
            "explorer.exe",
            f"shell:AppsFolder\\{appid}"
        ]
    )

        return True

    except Exception as e:

        print(
            "LAUNCH ERROR:",
            e
        )

        return False
    
def close_app(app_name):
        app = find_app(app_name)
        if not app:
            return False

        try:

            appid = app["appid"]

            print("APPID:", appid)

            # Extract useful identifiers from the AppID
            identifiers = []

            # Full AppID
            identifiers.append(appid.lower())

            # App name
            identifiers.append(app["name"].lower())

            # Search running Windows processes
            result = subprocess.run(
                [
                    "powershell",
                    "-Command",
                    """
                    Get-CimInstance Win32_Process |
                    Select-Object ProcessId,Name,ExecutablePath,CommandLine |
                    ConvertTo-Json -Compress
                    """
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )

            if not result.stdout.strip():
                return False

            processes = json.loads(result.stdout)

            if isinstance(processes, dict):
                processes = [processes]

                app_name_lower = app["name"].lower()

                matched_pids = []

            for process in processes:

                name = (process.get("Name") or "").lower()
                path = (process.get("ExecutablePath") or "").lower()
                cmd = (process.get("CommandLine") or "").lower()

                if (
                    app_name_lower in name
                    or app_name_lower in path
                    or app_name_lower in cmd
                ):
                        matched_pids.append(
                        process["ProcessId"]
                    )

            if not matched_pids:
                return False

            for pid in matched_pids:

                try:

                    subprocess.run(
                        [
                            "taskkill",
                            "/PID",
                            str(pid),
                            "/T",
                            "/F"
                        ],
                        capture_output=True,
                        text=True
                    )

                except Exception:
                    pass

            return True

        except Exception as e:

            print(
                "CLOSE ERROR:",
                e
            )

            return False