# 进程通信
# 通信是通过同一个 args
from multiprocessing import Process, Queue
from time import sleep


def download(q):
    imglist = ['a.jpg', 'b.jpg', 'c.jpg', 'd.jpg', 'e.jpg']
    for img in imglist:
        print('正在下载: ', img)
        sleep(0.5)
        # 放入
        q.put(img)


def getfile(q):
    while True:
        try:
            # 获取
            file = q.get(timeout=5)
            print('{} 保存成功'.format(file))
        except:
            print('全部保存完毕·········')
            break


if __name__ == '__main__':
    # 通信桥梁
    q = Queue(5)

    down = Process(target=download, args=(q,))
    gets = Process(target=getfile, args=(q,))
    # 创建进程
    down.start()
    # down 阻塞
    down.join()

    gets.start()
    gets.join()
