from  flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.jinja.html'), 200   # 200static code狀態對就200不寫也預設200


@app.route("/login",methods=['GET', 'POST'])   
def login():
    return render_template('login.jinja.html')
