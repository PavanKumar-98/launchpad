import pprint


class ToDoList:
	def __init__(self):
		self.list_name = ""
		self.to_do = []
		self.done = []
		
	
	def add(self):
		
		self.list_name = input("enter the task ")
		self.to_do.append(self.list_name)


	def markdone(self):
		
		print(self.to_do)
		i = int(input("enter the task number which is done"))
		i = i-1
		j = self.to_do[i]
		self.done.append(j)
		self.to_do.pop(i)
		


	def see_tasks(self):
		print(f"To do list {self.to_do}")
		print(f"done list{self.done}")

task_list = ToDoList()

while True:
	ch = int(input("What would you like to do\n\
	1. add a task \n\
	2. mark a finished task\n\
	3. see the tasks \n"))

	if ch == 1:
		task_list.add()

	elif ch == 2:
		task_list.markdone()

	elif ch == 3:
		task_list.see_tasks()

	else:
		break


	
