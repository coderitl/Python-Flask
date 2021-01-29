# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, flash, redirect, url_for
import settings

# 宏 和 模板的使用
app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/useBase')
def useBase():
    return render_template('useBase.html')


if __name__ == '__main__':
    print(app.url_map)
    app.run(port = 9000)  # 设置端口号最好在启动之前设置
