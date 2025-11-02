from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024  # Allow up to 10KB payloads

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        print("Received:", data)
        return jsonify({"status": "received"}), 200
    except Exception as e:
        print("Webhook error:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "BANKNIFTY sniper server is live!"

if __name__ == '__main__':
    app.run()
