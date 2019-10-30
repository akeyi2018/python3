from flask import Flask

# Flaskのインスタンスの作成
app = Flask(__name__)

# 「/」にアクセスしたときの処理
# 「Hello World!」を表示する
@app.route("/")
def hello():
    return "Hello World!"

# メイン関数
if __name__ == "__main__":
    app.run("0.0.0.0")
