from flask import Flask

# 导入配置文件
import settings

# 导入蓝图 对象
from apps.user.view import user_bp
from exts import db


def create_app():
    app = Flask(__name__, template_folder = '../templates', static_folder = '../static')  # app 是一个核心对象
    app.config.from_object(settings)  # 加载配置
    # 蓝图
    # 注册蓝图
    app.register_blueprint(user_bp)  # 将蓝图对象绑定到 app 上
    db.init_app(app) # 将 db 对象与 app 进行关联
    print(app.url_map)
    return app
