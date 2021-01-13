# 协程案例
import urllib  # 错误
import gevent

'''
erro: 由于暂时不了解爬虫,错误无法排除 
date: 2021.01.13 13:40:31 

python: 完结 python 基础学习
'''

# 猴子补丁
from gevent import monkey

monkey.patch_all()


def downUrl(url):
    response = urllib.request.urlopen(url)
    content = response.read()
    print('下载了{} 的数据,长度是:{}'.format(url, len(content)))


if __name__ == '__main__':
    urls = ['http://www.163.com', 'http://www.qq.com', 'http://www.baidu.com']
    g1 = gevent.spawn(downUrl, urls[0])
    g2 = gevent.spawn(downUrl, urls[1])
    g3 = gevent.spawn(downUrl, urls[2])

    g1.join()
    g2.join()
    g3.join()
