import redis
from lib.db import *


class MyRedis(object):
    def __init__(self, host='127.0.0.1', port='6379', password=''):
        self.pool = redis.ConnectionPool(host=host, port=port, password=password)
        self.r = redis.Redis(connection_pool=self.pool)

    # 根据key获取value值
    def get(self, k):
        return self.r.get(k)

    # 添加键值对
    def set(self, k, v):
        self.r.set(k, v)

    # 获取hash类型所有的key
    def get_hash_keys(self, name):
        data = self.r.hkeys(name)
        return data

    def get_hash_value(self, name, key):
        data = self.r.hget(name, key)
        return data

    def get_keys(self, name):
        data = self.r.keys(name)
        return data

    def get_value(self, name):
        value = self.r.get(name)
        return value

    def is_exists(self, key):
        return self.r.exists(key)

    def get_value_num(self, name, start=0, stop=100, withscores=True):
        return self.r.zrevrange(name, start, stop, withscores)

    # 删除KEY值
    def delete_key(self, k):
        tag = self.r.exists(k)  # 判断这个key是否存在
        if tag:
            self.r.delete(k)
            print('删除Key值(缓存)成功')
        else:
            print('这个key不存在')

    # 将name对应的hash中指定key的键值对删除
    def hash_del(self, name, k):
        res = self.r.hdel(name, k)
        if res:
            print('删除成功')
            return 1
        else:
            print('删除失败，该key不存在')
            return 0

    def get_type(self, key):
        attribute = self.r.type(key)
        return attribute

    # 给feed加互动分
    def add_feed_socre(self, name, num):
        data = self.r.zincrby(name, num)
        if data:
            print('加分成功')
        return data


# 关闭数据库&redis连接
def out_ssh_sql():
    os.popen("ps uax |grep ssh|grep -Ev 'grep|ssh-agent'|awk '{print $2}'|xargs kill")
    time.sleep(3)
