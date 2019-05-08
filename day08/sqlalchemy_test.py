# @Time : 2019/5/8 15:42
# @Author : 2273360936@qq.com
# @FileName : sqlalchemy_test.py
# @GitHub : https://github.com/liulichao1/python-0426
from sqlalchemy import Column, INTEGER, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    # toString()
    def __str__(self):
        print(self.id, self.email, self.password)
        return ''


engine = create_engine("mysql+ mysqlconnector://root:chao0309@ @localhost:3306/db_python")

DBSession = sessionmaker(bind=engine)

spike = User(email='Mike@mike.com', password='789')

session = DBSession()

session.add(spike)

session.commit()
