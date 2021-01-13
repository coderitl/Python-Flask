'''
conda解释器安装 gevent:
    conda install gevent
成功后显示:  All requested packages already installed.

全局解释器安装: pip/pip3 install gevent

greenlet已经实现了协程，但是这个工人切换，是不是觉得太麻烦了，不要着急，python还有一个比greenlet更强大的并且能够自动切换任务的模块`gevent`
其原理是当一个greentlet遇到IO（指的是input ouput输入输出，比如网络、文件操作等）操作时，比如访问网络，就自动切换到其他的greenlet,
等到 IO 完成，再适当的时候切换回来继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent我们自动切换协程，就保证总有greenlet在运行，而不是等待IO
'''
from greenlet import greenlet
import gevent
import time

# 猴子补丁
from gevent import monkey
monkey.patch_all()


def a():
    for i in range(5):
        print('A' + str(i))
        time.sleep(0.1)


def b():
    for i in range(5):
        print('B' + str(i))
        time.sleep(0.2)


def c():
    for i in range(5):
        print('C' + str(i))
        time.sleep(0.3)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()

'''
没有猴子补丁的输出: A0 A1 A2 A3 A4 B0 B1 B2 B3 B4 C0 C1 C2 C3 C4

添加猴子补丁后输出: A0 B0 C0 A1 B1 A2 C1 A3 B2 A4 B3 C2 B4 C3 C4 # 实现协程

'''