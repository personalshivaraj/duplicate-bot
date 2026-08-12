import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

seen_messages = set()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "👋 Hello! I am your Duplicate Cleaner Bot.\n"
        "Make me an Admin in your Channel or Group, and I will automatically delete duplicate posts and files!",
    )


# Channel Posts ke liye duplicate remover
@bot.channel_post_handler(
    content_types=["text", "photo", "document", "video", "audio"]
)
def handle_channel_posts(message):
    process_duplicate(message)


# Groups/Supergroups ke liye duplicate remover
@bot.message_handler(
    func=lambda message: True,
    content_types=["text", "photo", "document", "video", "audio"],
)
def handle_group_messages(message):
    if message.chat.type in ["group", "supergroup"]:
        process_duplicate(message)


# Common logic duplicate check aur delete karne ke liye
def process_duplicate(message):
    content = message.text or message.caption

    if not content and message.document:
        content = message.document.file_unique_id
    elif not content and message.photo:
        content = message.photo[-1].file_unique_id

    if content:
        if content in seen_messages:
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except Exception as e:
                print(f"Error deleting message: {e}")
        else:
            seen_messages.add(content)


if __name__ == "__main__":
    print("Bot Successfully Started!")
    bot.infinity_polling()
    
