"""

Custom forwarder for remain anonymous forwarding support

"""

from datetime import datetime
from typing import Iterable, List, Optional, Union

import pyrogram
from pyrogram import raw, types, utils


async def forward_messages(
    client: "pyrogram.Client",
    chat_id: Union[int, str],
    from_chat_id: Union[int, str],
    message_ids: Union[int, Iterable[int]],
    disable_notification: bool = None,
    schedule_date: datetime = None,
    protect_content: bool = None,
    drop_author: Optional[bool] = None,
    drop_media_captions: Optional[bool] = None
) -> Union["types.Message", List["types.Message"]]:
    """Forward messages of any kind.

    .. include:: /_includes/usable-by/users-bots.rst

    Parameters:
        client (``pyrogram.Client``):
            Pyrogram client.

        chat_id (``int`` | ``str``):
            Unique identifier (int) or username (str) of the target chat.
            For your personal cloud (Saved Messages) you can simply use "me" or "self".
            For a contact that exists in your Telegram address book you can use his phone number (str).

        from_chat_id (``int`` | ``str``):
            Unique identifier (int) or username (str) of the source chat where the original message was sent.
            For your personal cloud (Saved Messages) you can simply use "me" or "self".
            For a contact that exists in your Telegram address book you can use his phone number (str).

        message_ids (``int`` | Iterable of ``int``):
            An iterable of message identifiers in the chat specified in *from_chat_id* or a single message id.

        disable_notification (``bool``, *optional*):
            Sends the message silently.
            Users will receive a notification with no sound.

        schedule_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when the message will be automatically sent.

        protect_content (``bool``, *optional*):
            Protects the contents of the sent message from forwarding and saving.

        drop_author (``bool``, *optional*):
            Drop author from a message

        drop_media_captions (``bool``, *optional*):
            Drop media_captions from a message

    Returns:
        :obj:`~pyrogram.types.Message` | List of :obj:`~pyrogram.types.Message`: In case *message_ids* was not
        a list, a single message is returned, otherwise a list of messages is returned.

    Example:
        .. code-block:: python

            # Forward a single message
            await app.forward_messages(to_chat, from_chat, 123)

            # Forward multiple messages at once
            await app.forward_messages(to_chat, from_chat, [1, 2, 3])
    """

    is_iterable = not isinstance(message_ids, int)
    message_ids = list(message_ids) if is_iterable else [message_ids]

    r = await client.invoke(
        raw.functions.messages.ForwardMessages(
            to_peer=await client.resolve_peer(chat_id),
            from_peer=await client.resolve_peer(from_chat_id),
            id=message_ids,
            silent=disable_notification or None,
            random_id=[client.rnd_id() for _ in message_ids],
            schedule_date=utils.datetime_to_timestamp(schedule_date),
            noforwards=protect_content,
            drop_author=drop_author,
            drop_media_captions=drop_media_captions,
        )
    )

    forwarded_messages = []

    users = {i.id: i for i in r.users}
    chats = {i.id: i for i in r.chats}

    for i in r.updates:
        if isinstance(
            i, (raw.types.UpdateNewMessage,
                raw.types.UpdateNewChannelMessage,
                raw.types.UpdateNewScheduledMessage)
        ):
            forwarded_messages.append(
                await types.Message._parse(
                    client, i.message,
                    users, chats
                )
            )

    return types.List(forwarded_messages) if is_iterable else forwarded_messages[0]
