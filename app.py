from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def get_data():
    # 一次返回多个随机数
    return jsonify({
        'a': random.randint(1, 100),
        'b': random.randint(101, 200),
        'c': random.randint(201, 300)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
