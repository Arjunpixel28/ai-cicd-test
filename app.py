# app.py - Run need fix here 

from flask import Flask, request
import os

app = Flask(__name__)

# Security Issue: Hardcoded credentials
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

# Bug: Variable typo
def calculate_total(items):
    total = 0
    for item in items:
        total += item.price  # Bug: price doesn't exist
    return totall  # Typo: should be 'total'

# Security Issue: SQL Injection vulnerability
@app.route('/user/<user_id>')
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL Injection risk
    return query

# Performance Issue: Inefficient loop
@app.route('/search')
def search():
    data = []
    for i in range(10000):
        for j in range(10000):  # Nested loop - bad performance
            data.append(i * j)
    return str(len(data))

# Missing error handling
@app.route('/divide')
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a / b  # Will crash if b=0
    return str(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Security: Debug mode in production
