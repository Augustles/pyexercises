#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_string = 'mysql://root:cxk517@localhost:3306' # 连接数据库的路径
engine = create_engine(db_string,echo = True) # 返回一个数据库引擎，echo为true回显sql语句
db_session = sessionmaker(bind=engine) # 生成一个数据库会话类
session = db_session() # 这个可以认为是一个数据库连接
print session.execute('show databases').fetchall() # 显示所有数据库,first()
