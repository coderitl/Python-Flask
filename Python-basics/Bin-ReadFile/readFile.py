# 实时读取文件 指定行数
# 定义 main 函数
import random


def writeContent():
    with open('content.txt', 'w') as stream:
        for i in range(101):
            stream.write(str(i) + '\n')
        print('写入成功!')


def readContent():
    with open('content.txt', 'r', encoding = "utf-8") as stream:
        data = stream.readlines()
        data1 = len(data)
        startLine = int(input('请输入读取行数起始值: '))
        lnum = startLine
        for line in data:
            lnum += 1
            if (lnum >= startLine) and (lnum <= data1):
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
