# Coroutine 协程
'''
协程: 耗时操作
协程（Coroutine），它也被称为微线程。
耗时操作: 网络请求 网络下载(爬虫), IO：文件的读写 阻塞

'''
from time import sleep

def task1():
    for i in range(3):
        print('A'+str(i))
        yield
        sleep(1)

def task2():
    for i in range(3):
        print('B' + str(i))
        yield
        sleep(2)

if __name__ == '__main__':
    # 生成器
    t1 = task1()
    t2 = task2()

    while True:
        try:
            next(t1)
            next(t2)
        except:
            break

