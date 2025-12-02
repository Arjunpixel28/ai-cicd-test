from flask import Flask, request, jsonify
import os
import sqlite3

app = Flask(__name__)

API_KEY = os.getenv("APP_API_KEY", "")

def calculate_total(items):
    total = 0
    for item in items:
        total += item.get("price", 0)
    return total

@app.route('/user/<int:user_id>')
def get_user(user_id):
    try:
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()

        # Safe parameterized query
        cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cur.fetchone()

        conn.close()
        return jsonify(result if result else {})
    except Exception as e:
        # Specific error message for database issue
        return jsonify({"error": "An error occurred while fetching user data"}), 500

@app.route('/search')
def search():
    # Efficient version of the original function
    data = list(range(2, 200001, 2))
    return str(len(data))

@app.route('/divide')
def divide():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 1))
        result = a / b
        return str(result)
    except ZeroDivisionError:
        return jsonify({"error": "division by zero is not allowed"}), 400
    except ValueError:
        return jsonify({"error": "invalid input, both arguments should be integers"}), 400

debug_mode = os.getenv("FLASK_DEBUG") == "1"

if __name__ == '__main__':
    app.run(debug=debug_mode, host='0.0.0.0')