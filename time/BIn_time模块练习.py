import time

print('--------------------------------- 重点 -------------------------------------')
# 时间戳
print(time.time())

# 延迟
time.sleep(3)

# 将元组的时间转成字符串
s = time.strftime('%Y-%m-%d')
print(s)

print('----------------------------------------------------------------------')

t = time.time()
print(t) # 1609993679.9369621

# 将时间戳转换成字符串
print(time.ctime(t)) # Thu Jan  7 12:27:59 2021

# 将时间戳转换成元组
t = time.localtime(t)
print(t)
print(t.tm_yday)
print(t.tm_hour)

# 将元组的转换成时间戳
print(time.mktime(t))

