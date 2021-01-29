from flask import Flask, render_template, request, flash
import settings
app = Flask(__name__)
app.config.from_object(settings)
# 消息闪现秘钥
app.secret_key = 'flask'


@app.route('/reigster', methods = ['GET', 'POST'])
def reigster():
    # 获取请求方式
    if request.method == 'POST':
        # 获取请求参数
        username = request.form.get('username')  # 获取表单提交的用户名
        password = request.form.get('password')  # 获取表单提交的密码
        repassword = request.form.get('repassword')  # 获取表单提交的密码
        print(''' 
            用户名: {}
            密码: {}
            重复输入: {}
            '''.format(username, password, repassword))
        # 判断参数是否填写 & 密码是否相同
        if not all([username, password, repassword]):
            print('参数不完整')
            flash(u'参数不完整')
        # 判断密码是否相同 不相同输入密码不一致
        elif password != repassword:
            print('两次输入不一致')
            flash(u'两次输入不一致')
        else:
            return 's'
    return render_template('index.html')