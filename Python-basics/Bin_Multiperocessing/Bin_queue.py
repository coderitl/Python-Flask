# 进程之间的通信
from multiprocessing import Pool
from multiprocessing import Queue

# queue 队列
'''
队列是一个先进先出（FIFO，First In First Out）或者说后进后出（LILO，Last In Last Out）的数据结构。
'''

q = Queue(5)
# 放入
q.put('1a')
q.put('2a')
q.put('3a')

q.put('4a')
q.put('5a')
print(q.qsize()) # 获取队列数
q.put('6a') # 阻塞 如果 queue 满了则只能等待,除非有 '空地' 则添加成功

q.full() # 判断队列是否已满
q.empty() # 判断队列是否位空

q.put('7a')
q.put('8a')
q.put('9a')

# 取出 源码查看参数  timeout=
q.get('1a')

q.put_nowait() # 不阻塞

# 进程之间的通信