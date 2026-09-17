import subprocess
import json

database = {
    "apps": {},
    "files": {},
    "folders": {}
}

print("Scanning installed applications...")

result = subprocess.run(
    [
        "powershell",
        "-Command",
        "Get-StartApps | ConvertTo-Json"
    ],
    capture_output=True,
    text=True,
    encoding="utf-8"
)

apps = json.loads(result.stdout)

for app in apps:

    name = app["Name"].lower().strip()

    database["apps"][name] = {
        "name": app["Name"],
        "appid": app["AppID"]
    }

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
    f"Saved {len(database['apps'])} applications."
)