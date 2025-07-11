import telebot
import os

# استدعاء توكن البوت من المتغير البيئي
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً! أنا بوت جاهز للعمل!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"أنت قلت: {message.text}")

bot.polling()

