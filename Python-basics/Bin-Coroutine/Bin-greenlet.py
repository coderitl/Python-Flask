# pip install greenlet 第三方需要下载
'''
conda: conda install greenlet # 进入  anaconda 安装的 Scripts下
windows: pip/pip3 install greenlet
'''
from greenlet import greenlet
import time


def a():
    for i in range(5):
        print('A' + str(i))
        gb.switch()
        time.sleep(0.1)


def b():
    for i in range(5):
        print('B' + str(i))
        gc.switch()
        time.sleep(0.2)


def c():
    for i in range(5):
        print('C' + str(i))
        ga.switch()
        time.sleep(0.3)


if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)
    # 需要调一下
    ga.switch()

'''
结果输出: A0 B0 C0 A1 B1 C1 A2 B2 C2 A3 B3 C3 A4 B4 C4
'''
