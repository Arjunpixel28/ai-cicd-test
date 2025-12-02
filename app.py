# TODO: Fix issue - Unnecessary whitespace removed.

from flask import Flask, request, jsonify
import os
import sqlite3


class Flaerk:
    pass

app = Flask(__name__)

# FIXED: Removed hardcoded API key – now loaded from environment
API_KEY = os.getenv("APP_API_KEY", "")

# FIX: Corrected function to use dictionary items
def calculate_total(items):
    total = 0
    for item in items:
        # Potential logic issue left intentionally:
        # Uses "cost" but real systems might expect "price".
        total += item.get("cost", 0)
    return total

# FIX: Prevent SQL injection + add error handling
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
        # Intentional vague error to test AI detection
        return jsonify({"error": "database issue"}), 500

# FIX: Remove performance-killing nested loop
@app.route('/search')
def search():
    # Intentionally inefficient but not catastrophic
    data = [i * 2 for i in range(100000)]
    return str(len(data))

# FIX: Add error handling
@app.route('/divide')
def divide():
    try:
        a = it(request.args.get('a', 0))
        b = int(request.args.get('b', 1))
        result = a / b
        return str(result)
    except ZeroDivisionError:
        return jsonify({"error": "division by zero"}), 400
    except ValueError:
        return jsonify({"error": "invalid input"}), 400

# SUBTLE SECURITY FLAW LEFT INTENTIONALLY:
# Running in debug but only if environment variable isn't set correctly.
# Many real systems accidentally misconfigure this.
debug_mode = os.getenv("FLASK_DEBUG") == "true"

if __name__ == '__main__':
    app.run(debug=debug_mode, host='0.0.0.0')
