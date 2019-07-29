from flask import Flask
# 从flask引入request实例
from flask import flash, render_template, request, abort

app = Flask(__name__)
# 使用flash时，需要使用app.secret_key='123'加密
app.secret_key = "123"

@app.route('/')
def hello_world():
    flash('hahahha')
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if not username:
        flash('please input username')
        return render_template('index.html')
    if not password:
        flash('please input password')
        return render_template('index.html')
    if username == 'haha' and password == '123':
        flash('login success')
        return render_template('index.html')
    else:
        flash('usename or password is wrong')
        return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/<id>')
def user(id):
    if int(id) == 1:
        return render_template('user.html')
    else:
        abort(404)

if __name__ == '__main__':
    app.run()
