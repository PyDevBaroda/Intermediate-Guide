import random
import sqlite3
conn = sqlite3.connect('emp.db')
cursor = conn.cursor()
class Employee(object):
	'Common class for all Employees'
	EmpId = 0
	EmpTotal = 0
	try:
		conn.execute("CREATE TABLE EMPLOYEE (ID INT NOT NULL, NAME TEXT NOT NULL, POST INT NOT NULL, SALARY REAL);")

	except sqlite3.OperationalError:
		pass

	def __init__(self,name,post,salary):
		self.name = name
		self.post = post
		self.salary = salary
		self.EmpId = random.randint(0,9)
		id = self.EmpId
		cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,POST,SALARY) VALUES ( ?,?,?,? )", (id,name,post,salary));
		cursor.execute("SELECT COUNT(*) FROM EMPLOYEE");
		result = cursor.fetchone()
		Employee.EmpTotal=result[0]
		conn.commit()

	def GetEmpDetail(self):
		return (self.EmpId, self.name, self.post, self.salary)

def dataentry():
	name = raw_input('Enter name: ')
	post = raw_input('Enter post: ')
	sal = raw_input('Enter sal: ')
	obj1 = Employee(name,post,sal)
	#obj2 = Employee("Dattani","Student",0)
	detail1 = obj1.GetEmpDetail()
	#detail2 = obj2.GetEmpDetail()
	print detail1
	#print detail2
	print 'Total Employees are %d' % Employee.EmpTotal


def main():
	print '\n'
	while 1:
		print '*'*20
		print 'Select your option'
		print '*'*20
		print '1. Insert New employee'
		inp = input('Enter Option: ')
		if inp == 1:
			dataentry()
		else: 
			print '\n Enter Correct Option'
main()
