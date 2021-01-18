# pymysql 的使用
import pymysql


# 生成文件 pip freeze > requirements.txt
# 依赖项安装: pip install -r requirements.txt

def main():
    conn = pymysql.connect(host = '127.0.0.1',
                           port = 3306,
                           user = 'root',
                           password = 'root',
                           db = 'student',
                           charset = 'utf8')
    try:
        # 获得游标对象
        with conn.cursor() as cursor:
            # execute 执行
            result = cursor.execute('insert into tb_emp values(1001,"张三",4500)')
            if result == 1:
                print('添加成功')
                # commit() 很重要 否则看不到响应结果
                conn.commit()
            else:
                print('添加失败，操作已经回滚···')
    except pymysql.MySQLError as error:
        print(e)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    a = main()
