from flask import Blueprint, render_template, request, redirect
from apps.user.model import User

user_bp = Blueprint('user', __name__)

users = []


# 定义路由 用户中心
@user_bp.route('/')
def user_center():
    return '用户中心'


# 用户登录
@user_bp.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        print(f'用户名: {username} 密码: {password} 手机号: {phone}')
        if password == repassword:
            # 用户名唯一
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg = '用户名存在')
            user = User(username, password, phone)
            users.append(user)
            return redirect('/')
    return render_template('user/login.html')


# 用户注册
@user_bp.route('/register', methods = ["GET", "POST"])
def register():
    return render_template('user/register.html')


# 用户退出
@user_bp.route('/loginout', methods = ["GET", "POST"])
def loginout():
    return render_template('user/loginout.html')
