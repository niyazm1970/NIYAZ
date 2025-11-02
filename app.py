import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024  # 10KB limit

TELEGRAM_TOKEN = '8475148547:AAGb6GoNeF0tzNoLCiJZe6bTL-kwIxczoIc'
CHAT_ID = '627052152'  # Your confirmed Telegram User ID

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        print("Received:", data)

        message = f"📈 {data['signal']} {data['ticker']} @ {data['price']} ({data['timestamp']})"
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, json=payload)

        return jsonify({"status": "sent"}), 200
    except Exception as e:
        print("Webhook error:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "BANKNIFTY sniper server is live!"
