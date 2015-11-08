#!/usr/bin/env python
#-*-coding:utf8-*-

#总调用接口
from dbapi import *
from workers import *


#定义向表中添加Manager发布的会议的函数
def Add_Meeting_table_to_db(instance):
	meetings = instance.Public_meet()
	Session = sessionmaker(bind=db)
	session = Session()
	for fileds in meetings:
		v = meetings[fileds]
		every_meeting = Meeting(title=fileds,content=v[0],leader=v[1],meeting_time=v[2])
		session.add(every_meeting)
		session.commit()
	session.close()

if __name__=='__main__':

	Tom = Managers()
	Tom.Add_meetings('company meeting','about salary increase','Mr.Wang','2015-11-11 14pm')
	Add_Meeting_table_to_db(Tom)
