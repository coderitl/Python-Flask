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


if __name__ == '__main__':
    print('主进程···········',os.getpid())

    # 子进程
    p1 = Process(target=task1, args=(1, 'p1'), name='任务一')
    print(p1.name)
    p1.start()

    p2 = Process(target=task2, args=(2, 'p2'), name='任务二')
    print(p2.name)
    p2.start()

'''
总结:
    process.start() 启动进程并执行任务
    process.run() 只是执行了任务但没有启动进程
    terminate() 终止
'''