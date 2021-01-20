# 实时读取文件 指定行数
# 定义 main 函数
import random


def writeContent():
    with open('content.txt', 'w') as stream:
        for i in range(101):
            stream.write(str(i) + '\n')
        print('写入成功!')


def readContent():
    # 上下文语法 读取文件 同级目录下有一个 content.txt 文件
    with open('content.txt', 'r',encoding = 'utf8') as stream:
        # 统计总行数
        totalLine = len(stream.readlines())
        # 读取位置
        startLine = int(input('请输入读取行数起始值: '))
        lnum = startLine
        # 从 startLine 开始 读取到 totalLine 结束 第一个循环读取的行数
        for line in stream:
            lnum += 1
            if (lnum >= startLine) and (lnum <= totalLine):
                print(line)
            else:
                print('读取结束···')
                break


def main():
    # 写入内容
    # writeContent()
    # 读取文件
    readContent()


if __name__ == '__main__':
    main()
