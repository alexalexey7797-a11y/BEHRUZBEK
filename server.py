from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "BEHRUZBEK AI server ishlayapti! 🤖"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")

    return jsonify({
        "reply": f"Sening xabaring: {message}"
    })

if __name__ == "__main__":
    app.run()
