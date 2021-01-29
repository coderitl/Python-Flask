# -*- coding:utf-8 -*-
from flask import Flask
from flask_script import Manager

import settings
from apps import create_app

app = create_app()
manager = Manager(app = app)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()  # 设置端口号最好在启动之前设置 python app.py runserver -p 5001 新型启动方式
