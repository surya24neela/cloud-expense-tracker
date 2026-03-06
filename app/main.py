from flask import Flask, request, jsonify
from app.database import expenses

app = Flask(__name__)

@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.json
    expenses.append(data)
    return jsonify({"message": "Expense added"}), 201

@app.route("/expenses", methods=["GET"])
def list_expenses():
    return jsonify(expenses), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
