from  flask import Flask,request

app = Flask(__name__)
@app.route("/")
def index():
    print(request.args.get('name'))
    print(request.args.get('name1'))
    print(request.args.get('name2'))
    return "Hello! World",200  #200static code狀態對就200不寫也預設200

