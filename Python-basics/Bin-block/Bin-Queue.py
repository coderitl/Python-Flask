# 线程间的通信
'''
生产者与消费者: 两个线程之间的通信

python 的 queue 模块中提供了同步的,包括 FIFO(先进先出)队列 Queue

LIFO(后入先出) 队列 LifoQueue 和优先级队列 PriorityQueue。这些队列都实现了锁原语(可以理解为原子操作，即要么不做,要么就全做),能够在多线程中直接使用

可以使用队列来实现线程间的同步
'''
import queue
import threading
import random
from time import sleep


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put('生产者产生的数据: %d' % num)
        print('生产者产生的数据: %d' % num)
        sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()  # task_done() 源码附有


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者获取到: %s' % item)
        sleep(4)
    # 完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    arr = []

    # 创建生产者
    th1 = threading.Thread(target=produce, args=(q,))
    th1.start()

    # 创建消费者
    th2 = threading.Thread(target=consume, args=(q,))
    th2.start()

    th1.join()
    th2.join()

    print('END···············')
