import asyncio
import os
from pyrogram import Client, filters

app = Client("my_bot", bot_token=os.environ.get("BOT_TOKEN"))
seen_messages = set()


@app.on_message(filters.group)
async def remove_duplicates(client, message):
    if message.text or message.caption:
        content = message.text or message.caption
        if content in seen_messages:
            try:
                await message.delete()
            except Exception:
                pass
        else:
            seen_messages.add(content)


async def main():
    async with app:
        await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
    
