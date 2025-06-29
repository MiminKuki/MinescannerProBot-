import os
import telebot
from predictor import analyze_image
from utils import download_image

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "🤖 Welcome to MinescannerProBot!

"
                          "Send me a clear Mines game screenshot to get predictions.
"
                          "I'll highlight danger and safe tiles using AI.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        file_path = download_image(bot, message)
        response = analyze_image(file_path)
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

bot.polling()