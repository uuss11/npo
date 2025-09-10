# main.py
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from bot_config import BOT_TOKEN
from handlers.message_handler import handle_message

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ البوت شغال الآن!")
app.run_polling()
