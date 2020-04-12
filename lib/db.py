import pymysql, time, os, sshtunnel


def ssh_sql():  # 跳板机
    ssh_ser = sshtunnel.SSHTunnelForwarder(ssh_host=('', 22),
                                           ssh_username='',
                                           ssh_pkey=(r"C:\Users\Administrator\.ssh\id_rsa"),
                                           remote_bind_address=('', 3306),
                                           local_bind_address=('127.0.0.1', 53333))

    return ssh_ser


def connect_mysql(sql, db):  # 操作数据库
    try:
        connects = pymysql.connect(
            host='127.0.0.1',
            port=53333,
            user='',
            passwd='',  # password也可以
            db=db,
            charset='utf8',  # 如果查询有中文需要指定数据库编码
            connect_timeout=6)  # 设置连接超时时间
    except Exception as e:
        print('连接数据库错误，错误为:%s' % e)  # 如果连接错误，则抛出异常错误内容
    else:
        cur = connects.cursor()  # 建立游标，有游标才能操作数据库
        if 'select' in sql:  # 如果在sql中
            try:
                cur.execute(sql)  # 查询数据库（读）
            except Exception as e:
                print('执行sql语句失败，错误是%s' % e)  # 抛出查询失败错误内容
            else:
                fet = cur.fetchall()  # 获取查询结果
                connects.close()  # 关闭数据库连接
                cur.close()  # 关闭游标连接
                return fet  # 返回查询结果
        else:
            try:
                cur.execute(sql)  # 更改数据库(写)
            except Exception as e:
                print('执行sql语句失败，错误是%s' % e)  # 抛出异常内容
            else:
                # 提交数据至数据库
                connects.commit()  # 提交更改
                connects.close()  # 关闭数据库连接
                cur.close()  # 关闭游标


def through_sql():  # 数据库穿透
    os.popen('nohup ssh -L 3334: '
             ' -N &')
    time.sleep(3)
    os.popen('nohup ssh -L 6379: '
             ' -N &')
    time.sleep(2)
