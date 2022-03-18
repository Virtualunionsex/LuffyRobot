#
# Copyright (C) 2021-2022 by AyiinXd@Github, < https://github.com/AyiinXd >.
#
# This file is part of < https://github.com/AyiinXd/AyiinMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/AyiinXd/AyiinMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from AyiinMusic import app
from AyiinMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = (
             f"**Aʏɪɪɴ Pʟᴀʏ Lᴏɢ**\n\n"
             f"**Cʜᴀᴛ :** {message.chat.title} [`{message.chat.id}`]\n"
             f"**Usᴇʀ :** {message.from_user.mention}\n"
             f"**Usᴇʀɴᴀᴍᴇ :** @{message.from_user.username}\n"
             f"**Usᴇʀ ID :** `{message.from_user.id}`\n"
             f"**Cʜᴀᴛ Lɪɴᴋ :** {chatusername}\n\n"
             f"**Qᴜᴇʀʏ :** {message.text}\n\n"
             f"**Sᴛʀᴇᴀᴍ Tʏᴘᴇ :** {streamtype}"
        )
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
