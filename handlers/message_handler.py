# handlers/message_handler.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.ai_request import ai_reply

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    reply_text = await ai_reply(user_text)
    await update.message.reply_text(reply_text)
