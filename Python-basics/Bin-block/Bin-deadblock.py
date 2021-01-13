# 死锁
'''
开发过程中，在线程间共享多个资源的时候,如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁.
尽管死锁很少发生,但一旦发生就会造成应用的停止响应,程序不做任何事情

避免死锁
解决:
    1. 重构代码
    2. 使用 timeout 参数
'''
from threading import Thread, Lock
from time import sleep

# -------------------------------------------------------- S: 死锁 ----------------------------------------------------

# 准备两把锁
lockA = Lock()
lockB = Lock()


# 自定义线程
class MyThreadA(Thread):
    def run(self):  # start()
        #  源码: def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
        if lockA.acquire():  # 如果可以获取锁则返回 True (源码可知)
            print(self.name + '拿到了A锁')
            sleep(0.1)
            if lockB.acquire(timeout=5):
                print(self.name + '又获取了B锁,原来还有A锁')
                lockB.release()  # 释放 B 锁
            lockA.release()  # 释放 A 锁


class MyThreadB(Thread):
    def run(self):  # start()
        #  源码: def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
        if lockB.acquire():  # 如果可以获取锁则返回 True (源码可知)
            print(self.name + '拿到了B锁')
            sleep(0.1)
            if lockA.acquire(timeout=5):
                print(self.name + '又获取了A锁,原来还有B锁')
                lockA.release()  # 释放 B 锁
            lockB.release()  # 释放 A 锁


if __name__ == '__main__':
    th1 = MyThreadA()
    th2 = MyThreadB()

    th1.start()
    th2.start()

# -------------------------------------------------------- E: 死锁 ----------------------------------------------------
