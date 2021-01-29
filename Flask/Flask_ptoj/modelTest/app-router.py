# -*- coding:utf-8 -*-
# 局部测试
from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return 'Hello World!'


data = {'a': 'a1', 'b': 'b1', 'c': 'c1'}


def index():
    return '<h1><font color="red">index Text</font></h1>'


app.add_url_rule('/index', view_func = index)


# 参数 str 类型
@app.route('/getValue/<key>')  # 默认 str 不需要添加数据类型
def getValue(key):
    return data.get(key)


# int 类型
@app.route('/add/<int:num>')  # 默认 str 不需要添加数据类型
def add(num):
    result = num + 10
    return str(result)


if __name__ == '__main__':
    app.run(port = 9000)  # 设置端口号最好在启动之前设置
