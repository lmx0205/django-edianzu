from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb()
Base = declarative_base()

engine = create_engine(
    'mysql+pymysql://root:lmx0205@localhost:3306/text', echo=True)

DBSession = sessionmaker(bind=engine)

session = DBSession()

class User(Base):
    __tablename__='user'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

# 创建新User对象:
new_user = User(id='1', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()


