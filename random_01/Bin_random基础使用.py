import random

# 随机小数
r = random.random()
print(r)

# 奇数 1--> 起始值 10--> 终点值 2--> 步进值
ran = random.randrange(1, 10, 2)
print(ran)

# 随机整数
ran = random.randint(1, 10)
print(ran)

# 随机选择
list1 = ['a', 'b', 'c', 'd']
ran = random.choice(list1)
print(ran)

# 洗牌
pai = ['红梅 A', '方片K', '黑2']
ran = random.shuffle(pai)
print(pai)


# 验证码案例
def fun():
    code = ''
    for i in range(4):
        # 随机整数
        ranNum = str(random.randint(0, 9))
        # A-Z
        ranUpperStr = chr(random.randint(65, 90))
        # a-z
        ranLowerStr = chr(random.randint(97, 122))
        # 存放大小写组合
        ranList = [ranNum, ranUpperStr, ranLowerStr]
        # 随机选择
        rChoice = random.choice(ranList)
        # 拼接得到最终组合
        code += rChoice
    return code

# 函数调用
code = fun()
# 输出
print(code)

# chr  ord
print(chr(65))  # Unicode --> str
print(ord('A')) # str --> Unicode