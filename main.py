"""

Forward messages from chat to other chat.

"""

import os

import pyrogram

# Envs
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
TARGET_CHAT_ID = int(os.environ.get("TARGET_CHAT_ID"))
FORWARD_CHAT_ID = int(os.environ.get("FORWARD_CHAT_ID"))

# Initialize Telegram client
client = pyrogram.Client(
    "account",
    api_id=API_ID,
    api_hash=API_HASH,
)


@client.on_message()
async def message_handler(_, message: pyrogram.types.Message):
    """
    Handle messages from target chat and forward this to forward chat.

    :param _:
    :param message: Message object
    """

    if message.chat.id != TARGET_CHAT_ID:
        return

    await message.forward(FORWARD_CHAT_ID)


# Start client
if __name__ == "__main__":
    client.run()
