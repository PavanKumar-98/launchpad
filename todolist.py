import pprint

to_do = []
done = []

class ToDoList:
	def __init__(self,list_name ,to_do ,done ):
		self.list_name = list_name
		self.to_do = to_do
		self.done = done
		
	
	def add():
		
		list_name =input("enter the task ")
		to_do.append(list_name)


	def markdone():
		
		pprint(to_do)
		i = int(input("enter the task number which is done"))
		done.append(to_do(i))
		to_do.pop(i)


	def see_tasks():
		pprint(to_do)
		pprint(done)

task_list = ToDoList

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


	