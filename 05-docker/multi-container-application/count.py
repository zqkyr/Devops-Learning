from flask import Flask

import redis

counter_store = redis.Redis(host="redis", port=6379)

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the multi-container application."

@app.route("/count")
def count():
    visits = counter_store.incr("visits")
    return f"This page has been visited {visits} times."

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)