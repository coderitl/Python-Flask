# 全局变量
# 进程练习源码 2021-01-11
from multiprocessing import Process
import os
from time import sleep


def task1(timer, name):
    while True:
        sleep(timer)
        print(os.getpid(), '--------------------> ', os.getppid())
        print('{}'.format(name))


def task2(timer, name):
    while True:
        sleep(timer)
        print(os.getpid(), '--------------------> ', os.getppid())
        print('{}'.format(name))


# 全局变量
number = 1

if __name__ == '__main__':
    print('主进程···········', os.getpid())

    # 子进程
    p1 = Process(target=task1, args=(1, 'p1'), name='任务一')
    print(p1.name)
    p1.start()

    p2 = Process(target=task2, args=(2, 'p2'), name='任务二')
    print(p2.name)
    p2.start()

    while True:
        number += 1
        sleep(0.2)
        if number == 10:
            # 终止进程
            p1.terminate()
            p2.terminate()
            break
        else:
            print('number: ', number)
