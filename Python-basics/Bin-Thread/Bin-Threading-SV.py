# SV: Shared variable
# 共享数据(会造成一定影响)
'''
线程是可以共享全局变量的
'''
import threading
from time import sleep

money = 1000


def run1():
    global money
    for i in range(100):
        money -= 1


def run2():
    global money
    for i in range(100):
        money -= 1


# -------------------------------------------------------- S: 买票案例 ---------------------------------------------
# 票
ticket = 1000 # 数值较小几乎不会影响


def run3():
    global ticket
    for i in range(100):
        sleep(0.1)
        ticket -= 1


# -------------------------------------------------------- E: 买票案例 ---------------------------------------------


if __name__ == '__main__':
    '''
    th1 = threading.Thread(target=run1, name='th1')
    th2 = threading.Thread(target=run2, name='th2')
    
    # 开启线程 1
    th1.start()
    # 开启线程 2
    th2.start()
    
    th1.join()
    th2.join()
    '''
    # 买票案例开启 4 个线程
    th1 = threading.Thread(target=run3, name='th1')
    th2 = threading.Thread(target=run3, name='th2')
    th4 = threading.Thread(target=run3, name='th3')
    th3 = threading.Thread(target=run3, name='th4')

    # 开启线程 1
    th1.start()
    # 开启线程 2
    th2.start()
    # 开启线程 3
    th3.start()
    # 开启线程 4
    th4.start()

    # 插队
    th1.join()
    th2.join()
    th3.join()
    th4.join()

    # 主进程任务
    print('money: ', money)
    print('ticket: ', ticket)
