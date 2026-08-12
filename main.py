import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

seen_messages = set()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "👋 Hello! Main Duplicate Message Cleaner Bot hoon.\n"
        "Mujhe apne group me Admin bana do, main duplicate messages saaf kar dunga!",
    )


@bot.message_handler(
    func=lambda message: True, content_types=["text", "photo", "document"]
)
def handle_messages(message):
    if message.chat.type in ["group", "supergroup"]:
        content = message.text or message.caption
        if content:
            if content in seen_messages:
                try:
                    bot.delete_message(message.chat.id, message.message_id)
                except Exception:
                    pass
            else:
                seen_messages.add(content)


if __name__ == "__main__":
    print("Bot Successfully Start Ho Gaya!")
    bot.infinity_polling()
    
