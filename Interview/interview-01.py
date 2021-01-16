t = (1, 2, [30, 40])
# t[2] += [50, 60]

# print(t)

'''
a. t变成(1, 2, [30, 40, 50, 60])
b. 因为tuple不支持对它的元素赋值，所以会抛出TypeError异常
c. 以上两个都不是
d. a和b都是对的 

result: d
TypeError: 'tuple' object does not support item assignment
注意:
 1. 不要把可变对象放在元组里面。
 2. 增量赋值不是一个原子操作。我们刚才也看到了，它虽然抛出了异常，但还是完成了操作。
'''
# --------------- 一 ----------------------
# 字典排序
dic = {'a': 26, 'g': 20, 'e': 22, 'c': 24}
print(sorted(dic.items(), key=lambda x: x[1]))


# -------------- 二 -----------------------
def value_high(key):
    return dic[key]


for key in sorted(dic, key=value_high):
    print(key, dic[key])

# ---------------- 三 ---------------------
l = []
for k, v in dic.items():
    l.append(v)
l.sort()
dic = {}
for i in l:
    for k, v in dic.items():
        if i == v:
            dic[k] = v
print(dic)
