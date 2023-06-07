from  flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    # 200static code狀態對就200不寫也預設200
    return render_template('index.jinja.html'), 200

