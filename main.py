"""

Forward messages from chat to other chat.

"""

import pyrogram

import settings
import forwarder

# Initialize Telegram client
client = pyrogram.Client(
    name=settings.SESSION_NAME,
    api_id=settings.API_ID,
    api_hash=settings.API_HASH,
    proxy=settings.PROXY if settings.PROXY["scheme"] else None,
    device_model="PC",
    system_version="Forwarder bot",
)


@client.on_message(pyrogram.filters.chat(settings.TARGET_CHAT_ID))
async def target_chat_handler(_, message: pyrogram.types.Message):
    """
    Handle messages from target chat and forward this to forward chat.

    :param _:
    :param message: Message object
    """

    await message.forward(settings.FORWARD_CHAT_ID)


@client.on_message(pyrogram.filters.chat(settings.FORWARD_CHAT_ID))
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

    await forwarder.forward_messages(
        client,
        chat_id=settings.TARGET_CHAT_ID,
        from_chat_id=settings.FORWARD_CHAT_ID,
        message_ids=message.id,
        drop_author=settings.FORWARD_ANONYMOUS,
    )


# Start client
if __name__ == "__main__":
    client.run()
