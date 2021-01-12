# 线程
# 线程是进程的一部分
import threading
from time import sleep

'''

创建线程？

如何使用线程？

'''


def download():
    imglist = ['a.jpg', 'b.jpg', 'c.jpg', 'd.jpg', 'e.jpg']
    for img in imglist:
        print('正在下载: ', img)
        sleep(0.5)
        print('下载成功: {}'.format(img))


def listenMusic():
    musics = ['a.mp3', 'b.mp3', 'c.mp3', 'd.mp3', 'e.mp3', 'f.mp3']
    for music in musics:
        print('正在听: {}'.format(music))
        sleep(0.6)


if __name__ == '__main__':
    # 创建线程
    '''
   Thread 源码: 
       def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
    '''
    th1 = threading.Thread(target=download)
    # 启动线程
    th1.start()

    # 创建第二个线程
    th2 = threading.Thread(target=listenMusic)
    # 启动线程
    th2.start()
