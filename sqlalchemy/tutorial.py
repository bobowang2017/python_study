# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, text, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Hello(Base):
    __tablename__ = 'hello'

    id = Column(String, primary_key=True)
    name = Column(String)
    address = Column(String)
    number = Column(String)

    def __repr__(self):
        return "<Product(id='%s', name='%s', address='%s', number='%s')>" % (self.id, self.name, self.address, self.number)

DB_CON_STR = 'mysql+mysqldb://root:root@localhost/test?charset=utf8'
engine = create_engine(DB_CON_STR, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
res = session.query(Hello).filter(text("id=111")).one()
print (res.id, res.name, res.address, res.number)