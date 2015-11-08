#!/usr/bin/env python
# -*- coding:utf8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker


db_conn = 'mysql://recp:123456@192.168.1.124'
db_server = 'use Meeting'
db = create_engine(db_conn)
db.execute(db_server)
Base = declarative_base()

'''定义三张表'''
#定义会议表
class Meeting(Base):
	__tablename__ = 'meetings'
	
	meeting_id = Column(Integer,primary_key=True)
	title = Column(String(100))
	content = Column(String(1024))
	leader = Column(String(10))
	meeting_time = Column(String(20))

Base.metadata.create_all(db)
