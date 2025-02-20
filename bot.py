# Forex-signal-bot
import json
import requests
from flask import Flask, request
from telegram import Bot

TOKEN = "binamachine_bot"
CHAT_ID = "1946942327"
WEBHOOK_SECRET = "your_secret_key"

bot = Bot(token=TOKEN)
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "secret" in data and data["secret"] == WEBHOOK_SECRET:
        signal_message = f"📊 *Trading Signal* 📊\n\n🔹 *Pair:* {data['pair']}\n🔹 *Timeframe:* {data['timeframe']}\n🔹 *Indicator:* {data['indicator']}\n🔹 *Signal:* {data['signal']}"
        bot.send_message(chat_id=CHAT_ID, text=signal_message, parse_mode="Markdown")
        return json.dumps({"status": "success"})
    return json.dumps({"status": "error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
