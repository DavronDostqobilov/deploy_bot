
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater, 
    Dispatcher, 
    CallbackContext, 
    Filters, 
    MessageHandler, 
    CommandHandler, 
    CallbackQueryHandler)

TOKEN = "6149369057:AAFwx8G3CHGlxC2UyXnUV0FkLTKP6F5IBwk"

def start(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = str(update.message.chat.id)
    bot.sendMessage(chat_id=chat_id, text="Assalomu alaykum! Xush kelipsiz.")
def echo(update: Update, context: CallbackContext):
    bot = context.bot
    text=update.message.text
    chat_id = str(update.message.chat.id)
    bot.sendMessage(chat_id=chat_id, text=text)

