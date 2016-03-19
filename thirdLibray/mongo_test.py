# coding=utf-8

import ConfigParser
import random  # 导入random
from pymongo import MongoClient  # 导入Mongoclient

# 连接mongodb，增insert，save删drop，remove改update查find
# config = ConfigParser.RawConfigParser()
# config.read(r'C:\Users\ieware\pyexercises\august.conf')  # r不解析\

# try:
#     dbhost = config.get('base', 'dbhost')
# except NoSectionError, e:
#     print e

db = MongoClient(dbhost).august  # 连接August数据库
# db.authenticate # 用户认证
print db.collection_names()  # show collections查询所有聚合名称
db.user.count()  # 统计user聚合中数据数量
db.user.drop()  # 清空user聚合
db.user.save({'id': 1, 'name': 'nana', 'age': '23'})  # 插入一个数据

# 插入多个数据
for id in range(2, 10):
    name = random.choice(['lily', 'tom', 'jack'])
    age = random.choice(['23', '34', '58'])
    db.user.insert({'id': id, 'name': name, 'age': age})

users = db.user.find()  # 查询user聚合下所有数据
db.user.update({'age':'23'},{'$set':{'age':'33'}},upsert=False,multi=False)  # 更改第一个'age'为'33',upsert不存在则会插入，multi批量更新
db.user.remove({'id':1})  # 删除'id'为1的数据
for x in users:
    print x['age'], x['name'], x['id']
