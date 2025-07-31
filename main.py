
import os
import requests
from flask import Flask, request

app = Flask(__name__)

GUPSHUP_API_KEY = os.getenv("GUPSHUP_API_KEY")
GUPSHUP_APP_NAME = os.getenv("GUPSHUP_APP_NAME")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

def send_to_gupshup(text, phone):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "apikey": GUPSHUP_API_KEY
    }
    data = {
        "channel": "whatsapp",
        "source": GUPSHUP_APP_NAME,
        "destination": phone,
        "message": text
    }
    requests.post(url, headers=headers, data=data)

@app.route("/gupshup-webhook", methods=["POST"])
def gupshup_webhook():
    data = request.json
    if data and data.get("type") == "message":
        text = data["payload"]["payload"]["text"]
        phone = data["payload"]["source"]
        send_to_telegram(f"From {phone}: {text}")
    return "OK", 200

@app.route("/telegram-webhook", methods=["POST"])
def telegram_webhook():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]
        if TELEGRAM_CHAT_ID and str(chat_id) == TELEGRAM_CHAT_ID:
            if "::" in text:
                phone, reply = text.split("::", 1)
                send_to_gupshup(reply.strip(), phone.strip())
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
