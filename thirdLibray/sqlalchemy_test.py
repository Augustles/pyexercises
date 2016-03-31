##sqlalchemy

####pip install sqlalchemy
####https://www.keakon.net/2012/12/03/SQLAlchemy%E4%BD%BF%E7%94%A8%E7%BB%8F%E9%AA%8C
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DB_CONNECT_STRING = 'mysql+mysqldb://root:nana@localhost/s?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
session.execute('create database abc')
session.execute('show databases').fetchall()
session.execute('use scrapy')
session.execute('select * from douban')
session.execute('select * from douban').first()
query = session.query(User) # 查询User表
