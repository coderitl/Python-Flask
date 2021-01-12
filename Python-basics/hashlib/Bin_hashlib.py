# 2021-01-07 17:39:31
import hashlib

# ord 字符转换为 Unincode 吗
print(ord('我'))
print(ord('很'))
print(ord('喜'))
print(ord('欢'))
print(ord('你'))
# 25105 24456 21916 27426 20320 29579 33673

print('--------------------- content: 2021-01-10 ------------------------')
# 空
print('--------------------- content: 2021-01-11 ------------------------')

# 加密算法
print('--------------------- Md5 ------------------------')
pwd = '123456'
# md5 不可逆 --> 单向
md5 = hashlib.md5(pwd.encode('utf-8'))
# 16 进制加密
print(md5.hexdigest())  # e10adc3949ba59abbe56e057f20f883e

print('------------------------- sha1 ----------------------------------')
sha1 = hashlib.sha1(pwd.encode('utf-8'))
# sha1 加密
print(sha1.hexdigest())  # 7c4a8d09ca3762af61e59520943dc26494f8941b

print('------------------------- sha256 ----------------------------------')
sha256 = hashlib.sha256(pwd.encode('utf-8'))
# sha1 加密
print(sha256.hexdigest())  # 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92

# 登录注册
str = '123456'
# encode
str_en = hashlib.sha256(str.encode('utf-8'))
# 加密
str_pwd = str_en.hexdigest()

str_list = []
str_list.append(str_pwd)

# 用户输入密码加密之后进行对比
user_input = input('请输入密码: ')
user_sha256 = hashlib.sha256(user_input.encode('utf-8'))
sha256_pwd = user_sha256.hexdigest()

for i in str_list:
    if sha256_pwd == i:
        print('登录成功!', i)
    else:
        print('请重新输入···')
