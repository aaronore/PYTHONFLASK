from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.jinja.html'), 200   # 200static code狀態對就200不寫也預設200


@app.route("/login",methods=['GET', 'POST'])   
def login():
    if request.args.get("error") != "":
        error = request.args.get("error")
    error = None
    if request.method == 'POST':
        if request.form['email'] == 'robert@gmail.com' and request.form['pwd'] == '12345':
            return redirect(url_for('index'))
        else:
            error = '密碼不正確'
            return redirect(url_for('login', error=error))
        
    return render_template('login.jinja.html', error=error)
