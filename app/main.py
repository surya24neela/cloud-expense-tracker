from flask import Flask, request, jsonify
from app.database import get_connection, init_db

app = Flask(__name__)

@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.json
    title = data.get("title")
    amount = data.get("amount")

    conn = get_connection()
    cur = conn.cursor()
    init_db()
    cur.execute(
        "INSERT INTO expenses (title, amount) VALUES (%s, %s)",
        (title, amount)
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Expense added"}), 201

@app.route("/expenses", methods=["GET"])
def list_expenses():
    conn = get_connection()
    cur = conn.cursor()
    init_db()
    cur.execute("SELECT id, title, amount FROM expenses")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    expenses = []
    for row in rows:
        expenses.append({
            "id": row[0],
            "title": row[1],
            "amount": row[2]
        })

    return jsonify(expenses), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
