# 输入相应参数
import pymysql


def main():
    conn = pymysql.connect(host = 'localhost',
                           port = 3306,
                           user = 'root',
                           passwd = 'root',
                           db = 'student',
                           charset = 'utf8',
                           cursorclass = pymysql.cursors.DictCursor)  # 修改类型
    try:
        # 获取游标对象
        with conn.cursor() as cursor:
            # 执行 sql 注意参数位置
            cursor.execute('select eno,ename,sal from tb_emp')
            # 元组类型结果集
            # for row in cursor.fetchall():
            #     print('''
            #     ----------- 查询所有 -------
            #     eno: {}
            #     ename: {}
            #     sal: {}
            #     -------------------------
            #
            #     '''.format(row[0], row[1], row[2]))

            # 字典类型结果集 如果查询时带别名, 那么字典的键要更改为 别名
            for row in cursor.fetchall():
                # print(row)
                print('''
                -------------------------
                eno: {}
                ename: {}
                sal: {}
                --------------------------
                '''.format(row['eno'], row['ename'], row['sal']))
    except pymysql.MySQLError as erro:
        print(erro)
    finally:
        # 关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
