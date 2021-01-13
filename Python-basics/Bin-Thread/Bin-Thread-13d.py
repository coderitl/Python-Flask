# 13d 2021.01.13
# 多线程同步
'''
数据共享:
    如果多个线程共同对某个数据修改，则可能出现不可预料的结果,为了保证数据的正确性,需要对多个线程进行同步

同步: 一个一个的完成,一个1做完另一个才能进来
    效率会降低

    使用 Thread 对象的 Lock 和 RLock 可以实现简单的线程同步,这个对象都有 acquire 方法 和 release方法,对于那些需要每次
    只允许一个线程操作的数据,可以将其操作放在 acquire 和 release 方法之间

    多线程的优势在于可以同时运行多个任务。但是当线程需要共享数据时,可能存在数据不同步的问题,为了避免这种情况,引入锁的概念

'''

import threading
from time import sleep
import random

# 锁对象
lock = threading.Lock()

# 可变类型
list1 = [0] * 10  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# --------------------------------- S: 加锁任务 ----------------------------------------------
def task1():
    # 获取线程锁,如果已经上锁,则等待锁的释放
    lock.acquire()  # 阻塞
    # 任务
    for i in range(len(list1)):
        list1[i] = 1
        sleep(0.5)
    lock.release()  # 释放锁


def task2():
    lock.acquire()  # 阻塞
    for i in range(len(list1)):
        print('--------------> ', i)
        sleep(0.5)
    lock.release()  # 释放锁


if __name__ == '__main__':
    # 创建线程
    th1 = threading.Thread(target=task1)
    th2 = threading.Thread(target=task2)

    # 开启线程
    th2.start()
    th1.start()

    # 阻塞
    th2.join()
    th1.join()

    print(list1)
# --------------------------------- E: 加锁任务 ----------------------------------------------
