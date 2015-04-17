#coding=utf-8

import ConfigParser
import random # 导入random
from pymongo import MongoClient # 导入Mongoclient

# 连接mongodb，增insert，save删drop改查find
config = ConfigParser.RawConfigParser()
config.read(r'C:\Users\ieware\pyexercises\august.conf')

try:
    dbhost=config.get('base','dbhost')
except NoSectionError, e:
    print e

db = MongoClient(dbhost).august #连接August数据库
#db.authenticate # 用户认证
print db.collection_names() # show collections
db.user.drop() # 清空user聚合
db.user.save({'id':1,'name':'nana','age':'23'}) # 插入一个数据

# 插入多个数据
for id in range(2,10):
    name = random.choice(['lily','tom','jack'])
    age = random.choice(['23','34','58'])
    db.user.insert({'id':id,'name':name,'age':age})

users = db.user.find() # 查询所有的user聚合
for x in users:
    print x['age'],x['name'],x['id']
