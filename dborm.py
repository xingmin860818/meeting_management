#!/usr/bin/env python
# -*- coding:utf8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,backref
import sqlalchemy
import config


db_conn = '{}://{}:{}@{}'.format(config.db_server,config.conn_user,config.password,config.conn_addr)
db_server = 'use {}'.format(config.createdb)
db = create_engine(db_conn)
db.execute(db_server)
Base = declarative_base()
Session = sessionmaker(bind=db)

'''定义三张表'''
#定义会议表
class User_regist(Base):
	__tablename__ = 'user'

	role = Column(String(10))
	user_name = Column(String(15),primary_key=True)
	password = Column(Integer)

class Meeting(Base):
	__tablename__ = 'meetings'
	
	id = Column(Integer,primary_key=True)
	title = Column(String(100))
	content = Column(String(1024))
	leader = Column(String(15))
	meeting_time = Column(String(20))

class User_sign(Base):
	__tablename__ = 'sign'

	user_id = Column(Integer,primary_key=True)
	meeting_title = Column(String(100),primary_key=True)
	user_name = Column(String(15))

class Comment_plateform(Base):
	__tablename__ = 'comment'

	id = Column(Integer,primary_key=True)
	user_name = Column(String(15))
	meeting_title = Column(String(100))
	user_comment = Column(String(1000))
Base.metadata.create_all(db)

#定义创建会话的装饰器
def makesession(func):
	def wrapper(self,*arg,**kwargs):
		session = Session()
		func(self,session,*arg,**kwargs)
		session.commit()
	return wrapper

#定义数据库的增删改查操作
class Database(object):
	def __init__(self,table):
		self.table = table
	@makesession
	def Add(self,session,**kwargs):
		keywards = self.table(**kwargs)
		session.add(keywards)
	@makesession
	def Del(self,session,ID):
		pass	
	@makesession
	def Update(self,session,title,chg_obj,chg_content):
		try:
			session.query(self.table).filter(self.table.title==title).update({chg_obj:chg_content})
			session.commit()
		except sqlalchemy.exc.InvalidRequestError:
			session.rollback()
			raise

d = Database(Meeting)
#d.Add(title='wangsir meeting2',content='let\'s play',leader='Mr.wang',meeting_time='2015-12-30')
d.Update('wangsir meeting2','leader','Mr.ldd')
