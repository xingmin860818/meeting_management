#!/usr/bin/env python
#-*-coding utf8-*-
#from meetings import Meetings
import time
#定义员工类
class Workers(object):
	def __init__(self):
		
		self.meetings = {}
	def Search_meet(self,title):
		pass
	def Sign_up(self):
		pass
	def Comment(self):
		pass
	def Look_patteners(self):
		pass
#定义管理员类，继承员工类
class Managers(Workers):
	def __init__(self):
		self.meeting = {}
	def Add_meetings(self,title,content,leader,meeting_time):
		self.meeting[title] = (content,leader,meeting_time)
	def Public_meet(self):
		return self.meeting
	def Delete_meetings(self):
		pass
	def Change_meeting(self):
		pass
	def __call__(self):
		return self.meeting
#定义普通员工类
class Customs(Workers):
		pass
	
