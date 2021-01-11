# 自定义进程 等待后续理解
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        # 复习 super()
        super(MyProcess, self).__init__()
        self.name = name

    # 自定义进程 需要重写 run 方法
    def run(self):
        pass
