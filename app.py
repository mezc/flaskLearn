#!/usr/bin/python
#coding:utf-8
from flask import Flask
from flask import request, render_template, flash, redirect

# 创建实例
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route("/user", methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if request.method == 'POST':
        if username == 'haha' and password == '123':
            print('i m logging')
            return redirect("http://www.jikexueyuan.com")
        else:
            message = "login failed"
            return render_template('index.html', message=message)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8081)