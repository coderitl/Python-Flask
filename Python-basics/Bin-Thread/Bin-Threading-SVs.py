# 锁
# GIL 全局解释器锁
'''
Global Interpreter Lock,缩写 GIL 是计算机程序设计语言解释器用于同步线程的一种机制，
它使得任何时刻仅有一个线程在执行。[1]即便在多核心处理器上，使用 GIL 的解释器也只允许同一时间执行一个线程。
常见的使用 GIL 的解释器有CPython与Ruby MRI。
'''
import threading

n = 0


def task1():
    global n
    for i in range(1000000):
        n += 1
    print('task1n: ', n)


def task2():
    global n
    for i in range(1000000):
        n += 1
    print('task2n: ', n)


if __name__ == '__main__':
    # 创建线程
    th1 = threading.Thread(target=task1)
    th2 = threading.Thread(target=task2)

    # 开启线程
    th1.start()
    th2.start()

    # 阻塞
    th1.join()
    th2.join()

    # 主进程
    print('n: ', n)
