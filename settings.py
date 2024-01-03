"""

Client settings

"""

import os

import dotenv

dotenv.load_dotenv()

SESSION_NAME = os.environ.get("SESSION_NAME", "account")

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

TARGET_CHAT_ID = int(os.environ.get("TARGET_CHAT_ID"))
FORWARD_CHAT_ID = int(os.environ.get("FORWARD_CHAT_ID"))

PROXY = {
    "scheme": os.environ.get("PROXY_SCHEME"),
    "hostname": os.environ.get("PROXY_HOST"),
    "port": int(os.environ.get("PROXY_PORT")),
    "username": os.environ.get("PROXY_USERNAME"),
    "password": os.environ.get("PROXY_PASSWORD"),
}
