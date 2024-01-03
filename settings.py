"""

Client settings

"""

import os

import dotenv


def is_true(val: str) -> bool:
    """
    Check a value is true or false.

    :param val:
    :return: True if value is true, False otherwise
    """
    return val.lower() in ["true", "1", "yes", "t"]


dotenv.load_dotenv()

SESSION_NAME = os.getenv("SESSION_NAME", "account")

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

TARGET_CHAT_ID = int(os.getenv("TARGET_CHAT_ID"))
FORWARD_CHAT_ID = int(os.getenv("FORWARD_CHAT_ID"))

FORWARD_ANONYMOUS = is_true(os.getenv("FORWARD_ANONYMOUS"))

PROXY = {
    "scheme": os.getenv("PROXY_TYPE"),
    "hostname": os.getenv("PROXY_HOST"),
    "port": int(os.getenv("PROXY_PORT")),
    "username": os.getenv("PROXY_USERNAME"),
    "password": os.getenv("PROXY_PASSWORD"),
}
