import asyncio

# Python 3.14 error fix: Pyrogram import hone se pehle event loop banana padta hai
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

import os
from pyrogram import Client, filters

app = Client("my_bot", bot_token=os.environ.get("BOT_TOKEN"))
seen_messages = set()


@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "👋 Hello! Main ek Duplicate Message Cleaner Bot hoon.\n\n"
        "Mujhe group me Admin bana do, duplicate kachra main saaf kar dunga!"
    )


@app.on_message(filters.group)
async def remove_duplicates(client, message):
    content = message.text or message.caption
    if content:
        if content in seen_messages:
            try:
                await message.delete()
            except Exception:
                pass
        else:
            seen_messages.add(content)


if __name__ == "__main__":
    print("Bot start ho raha hai...")
    app.run()
    
