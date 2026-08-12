import asyncio
import os
from pyrogram import Client, filters

app = Client("my_bot", bot_token=os.environ.get("BOT_TOKEN"))
seen_messages = set()


# Start Command
@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "👋 Hello!\n\n"
        "Main ek **Duplicate Message Cleaner Bot** hoon.\n"
        "Mujhe apne group me add karein aur **Admin** banayein (Delete Messages ki permission ke sath), phir main saare duplicate messages apne aap delete kar dunga!"
    )


# Help Command
@app.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text(
        "🛠 **Help Menu:**\n\n"
        "• Main kisi bhi group me duplicate text ya photos ko repeat hone se rokta hoon.\n"
        "• Mujhe bas group ka Admin banana zaroori hai."
    )


# Duplicate Deletion Logic (Group ke liye)
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
    
