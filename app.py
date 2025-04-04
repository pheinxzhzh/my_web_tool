import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 读取 Render 指定的端口
    app.run(host="0.0.0.0", port=port)        # 绑定到所有 IP（对外开放）
