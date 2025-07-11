import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# إعدادات السجل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# التوكن الخاص بالبوت
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # ← سيتم استبداله لاحقًا

# أسماء المستخدمين المصرح لهم باستخدام البوت
ALLOWED_USERS = [
    "tayoob07_bot",  # ← أضف أي اسم مستخدم آخر هنا
    "tayoob_private",
    "mysecondbot"
]

# أمر البدء
def start(update: Update, context: CallbackContext):
    username = update.effective_user.username
    if username not in ALLOWED_USERS:
        update.message.reply_text("🚫 غير مصرح لك باستخدام هذا البوت.")
        return
    update.message.reply_text("مرحباً! أرسل /movers للحصول على تحركات السوق.")

# أمر تحركات السوق
def movers(update: Update, context: CallbackContext):
    username = update.effective_user.username
    if username not in ALLOWED_USERS:
        update.message.reply_text("🚫 غير مصرح لك باستخدام هذا البوت.")
        return
    message = "📈 تحركات السوق:\n\nAAPL: $150.25 (+1.5%)\nTSLA: $720.12 (-2.3%)\nAMZN: $3345.55 (+0.8%)"
    update.message.reply_text(message)

# تشغيل البوت
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("movers", movers))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
