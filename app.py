from flask import Flask
# 从flask引入request实例
from flask import request, url_for, render_template
from modules import User


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'

# 引入类
@app.route('/user')
def user():
    user = User(10001, "alex")
    return render_template('user_index.html', user=user)

# 模版中的参数传递
@app.route('/query_id/<id>')
def user_id(id):
    user = None
    if int(id) == 1:
        user = User(1, 'hahahhaha')

    return render_template('user_id.html', user=user)

@app.route('/users')
def user_list():
    user_li = []
    for i in range(10):
        user = User(i, "haha_{}".format(str(i)))
        user_li.append(user)
    return render_template('user_list.html', user_li=user_li)

@app.route('/base_one')
def base_one():
    return render_template('base_one.html')

@app.route('/base_two')
def base_two():
    return render_template('base_two.html')

if __name__ == '__main__':
    app.run()
