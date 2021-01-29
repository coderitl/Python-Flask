# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, flash, redirect, url_for
import settings

app = Flask(__name__)
app.config.from_object(settings)


# --------------------------------- 自定义过滤器 -------------------------------
# 自定义过滤器 本质是函数
def replace_str(value):
    value = value.replace('str', '我被替换了···')
    return value.strip()


# 过滤器
app.add_template_filter(replace_str, 'replace')


# ----------------------------- 装饰器定义过滤器 -----------------------
@app.template_filter('listreverse')
def reverse_filter(li):
    temp_li = list(li)
    li = temp_li.reverse()
    return temp_li


# ---------------------------------------------------------------------
@app.route('/define_filter')
def define_filter():
    msg = 'str 在 str 中'
    li = [2, 6, 7, 8]
    return render_template('define_filter.html', msg = msg, li = li)


if __name__ == '__main__':
    app.run(port = 9000)  # 设置端口号最好在启动之前设置
