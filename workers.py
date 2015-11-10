
	
#!/usr/bin/env python
#-*-coding:utf8-*-
'''用于人员控制，员工基类，管理员和普通员工继承基类，获得
基类的基本功能，管理员在基本功能之上具有会议修改权'''
from meetings import *
from sign_up import Sign_user

class Workers(object):
	'''基类具有管理员和普通员工共有的方法'''
	def __init__(self):
		#初始化接口实例
		self.meet = Meeting_manage()
		self.sign = Sign_user()
	def Search_meet(self):
		#从会议接口中查询会议
		result = self.meet.Search_meeting_from_db()
		return result
	def Sign_up(self,meeting_title,user_name):
		#用户注册
		self.sign.Sign_up(meeting_title,user_name)
	def Look_patteners(self,meeting_title):
		#从用户接口中查询相同会议参会人
		lis = []
		sign_users = {}
		users = self.sign.Show_meet_users(meeting_title)
                for name in users:
		       lis.append(name[0])
		sign_users[meeting_title]=lis
		return sign_users
	def Comment(self):
		pass
class Managers(Workers):
	'''管理员拥有对会议的增删改功能'''
	def __init__(self):
		super(Managers,self).__init__()
	def Add_meetings(self,title,content,leader,meeting_time):
		#新增会议
		self.meet.Add_meeting_to_db(title,content,leader,meeting_time)
	def Delete_meetings(self,ID):
		#通过会议id号删除过期会议
		self.meet.Del_meeting_from_db(ID)
	def Update_meeting(self,content,chg_obj,chg_content):
		#更改已发布会议内容
		self.meet.Update_meeting_to_db('company meeting','content','changed content')
	def Del_user(self,ID):
		#对参会报名人员表进行人员管理
		self.sign.Del_user(ID)

class Customs(Workers):
	'''普通用户暂时不需要定制功能'''
	def __init__(self):
		super(Customs,self).__init__()
