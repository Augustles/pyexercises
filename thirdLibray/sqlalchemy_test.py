# sqlalchemy

# pip install sqlalchemy
# https://www.keakon.net/2012/12/03/SQLAlchemy%E4%BD%BF%E7%94%A8%E7%BB%8F%E9%AA%8C
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, create_session
DB_CONNECT_STRING = 'mysql+mysqldb://root:nana@localhost/s?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
session.execute('create database abc')
session.execute('show databases').fetchall()
session.execute('use scrapy')
session.execute('select * from douban')
session.execute('select * from douban').first()
query = session.query(User)  # 查询User表
q = query.filter_by(uri_doc_index=item['uri_doc_index'], download_uri=item[
                    'download_uri'])  # 查询uri_doc_index和url
q.all(), q.first()  # 全部和第一个元素
q.delete(synchronize_session=False)  # synchronize_session必须为False, 否则会报错
metadata = MetaData(engine)
tb_document = Table('tb_document', metadata, autoload=True)
session = create_session()
query = session.query(tb_document)
