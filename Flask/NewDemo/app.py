from flask import Flask, render_template

# 导入配置信息
from flask_sqlalchemy import SQLAlchemy

import settings
# 表单所需
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config.from_object(settings)


db = SQLAlchemy(app)

class LoginForm(FlaskForm):
    username = StringField(u'用户名')
    password = PasswordField(u'密码')
    repassword = PasswordField(u'确认密码')
    submit = SubmitField(u'提交')


@app.route('/', methods = ["GET", "POST"])
def index():
    # 变量传值
    loginform = LoginForm()
    return render_template('index.html',form = loginform)


if __name__ == '__main__':
    app.run()
