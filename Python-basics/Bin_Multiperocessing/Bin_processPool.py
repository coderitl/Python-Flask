# 进程池
'''
当需要创建的子进程数量不多时,可以直接利用 multiprocessing 中的 Process 动态生成多个进程
但如果是上百甚至上千个目标,手动的的去创建进程的工作量巨大,此时就可以用到 multiprocessing 模块提供的 Pool 方法
初始化 Pool 时,可以指定一个最大进程数,当有新的请求提交到 Pool 时,如果池还没有满,那么就会创建一个新的进程来执行该请求,但
如果池中的进程数已经达到指定的最大值,那么该请就就会等待,直到池中有进程结束,才会创建新的进程来执行

非阻塞式: 全部添加到队列中,立刻返回,并没有等待其他的进程完毕,但是回调函数是等待任务完成后才调用
阻塞式: 区别在 apply()  apply_async()
回调函数:
'''
from multiprocessing import Pool
import os
import time
import random


def task_fun(task_name):
    print('任务开始啦·············', task_name, os.getpid())
    # 获取时间戳
    start = time.time()
    # 使用 sleep
    time.sleep(3)
    end = time.time()
    print('用时: {}'.format(start - end))
    # 需要 return
    return '用时: {}'.format(start - end)


def callback_fun(n):
    # 必须添加参数
    container_list.append(n)


container_list = []

if __name__ == '__main__':
    # 创建进程池 开启 5 个子进程
    pool = Pool(5)
    '''
    源码,Pool 中的参数: 
    def Pool(processes: Optional[int] = ..., # 最大进程数 整数类型
             initializer: Optional[Callable[..., Any]] = ...,
             initargs: Iterable[Any] = ...,
             maxtasksperchild: Optional[int] = ...) -> pool.Pool: ...
    '''
    list = ['1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a']
    for task in list:
        # 非阻塞式
        pool.apply_async(task_fun, args=(task,), callback=callback_fun)
    pool.close()  # 添加任务结束
    pool.join()  # 堵住主进程 插队，不会执行后续 over,会等待 子进程执行完毕··········

    # 主进程任务
    for i in container_list:
        print(i)

