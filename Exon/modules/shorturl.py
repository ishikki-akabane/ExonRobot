from pyrogram import filters
from pyrogram.types import Message

from Exon import pgram as Bot
import pyshorteners


@Bot.on_message(filters.command("shorturll"))
async def urlshortner(client, message):
    msg_text = message.text
    if len(msg_text.split(" ")) < 2:
        await message.reply_text(
            f"Please give me link to create a shortlink!"
        )
        return
    url = msg.text.split(None, 1)[1]
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    await message.reply_text(
        f"Here is your short link\n: <code>{short_url}</code>"
    )
