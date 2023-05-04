from flask import Flask, request
from telegram import Update
from telegram.ext import Dispatcher, Updater, MessageHandler, CommandHandler, Filters
import telegram
from bot import start, echo

app = Flask(__name__)
TOKEN = "6149369057:AAFwx8G3CHGlxC2UyXnUV0FkLTKP6F5IBwk"
bot = telegram.Bot(TOKEN)

@app.route("/")
def main():
    return "DEPLYMENT"

@app.route("/webhook", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        data = request.get_json(force=True)
        dp = Dispatcher(bot, None, workers=0)

        update = Update.de_json(data, bot)

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text, echo))

        dp.process_update(update)
        return "OK"
    else:
        return "Not allowed GET request"
    

if __name__ == "__main__":
    app.run(debug=True)