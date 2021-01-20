# 输入相应参数
import pymysql


def main():
    conn = pymysql.connect(host = 'localhost',
                           port = 3306,
                           user = 'root',
                           passwd = 'root',
                           db = 'student',
                           charset = 'utf8')
    oldeno = int(input('请输入编号: '))

    try:
        # 获取游标对象
        with conn.cursor() as cursor:
            # 执行 sql
            result = cursor.execute('update  tb_emp set eno =%s where eno=%s', (eno,))
            if result == 1:
                print('更新数据成功···')
                conn.commit()
            else:
                print('更新数据失败,操作已经回滚····')
    except pymysql.MySQLError as erro:
        print(erro)
        # 回滚
        conn.rollback()
    finally:
        # 关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
