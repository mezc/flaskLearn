from flask import Flask
# 从flask引入request实例
from flask import request, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# 换请求方式
@app.route('/user', methods=['POST'])
def hello_user():
    return 'Hello User!'

# 传递参数
@app.route('/user/<id>')
def hello_id(id):
    return 'Hello id:{}'.format(id)

@app.route('/query_user')
def query_id():
    id = request.args.get('id')
    # 访问：http://127.0.0.1:5000/query_user?id=12345
    return 'query_user id:{}'.format(id)

# 方向路由：通过视图函数，反找出url地址
@app.route('/query_url')
def query_url():
    # 访问：http://127.0.0.1:5000/query_url
    return 'query_url:{}'.format(url_for('query_id'))

if __name__ == '__main__':
    app.run()
