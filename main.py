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


@client.on_message(pyrogram.filters.chat(TARGET_CHAT_ID))
async def target_chat_handler(_, message: pyrogram.types.Message):
    """
    Handle messages from target chat and forward this to forward chat.

    :param _:
    :param message: Message object
    """

    await message.forward(FORWARD_CHAT_ID)


@client.on_message(pyrogram.filters.chat(FORWARD_CHAT_ID))
async def forward_chat_handler(_, message: pyrogram.types.Message):
    """
    Handle messages from forward chat and forward this to target chat.

    :param _:
    :param message: Message object
    """

    if not message.reply_to_message:
        return
    if not message.reply_to_message.forward_from:
        return
    if message.reply_to_message.from_user.id != client.me.id:
        return

    await message.forward(TARGET_CHAT_ID)


# Start client
if __name__ == "__main__":
    client.run()
