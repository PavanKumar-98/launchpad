database = {}
Math = 0
Physics = 1
Chemistry = 2
Biology = 3
Social_Science = 4
x=0
while True:
	name = input("enter the name \n")
	subject = input("enter the subject with spaces\n")
	if name == "":
		break

	marks = list(subject.split())
	database[name] = marks

sname = input("enter the name\n")
ssub = input("enter sub\n ")

if ssub == "Math":
	x = 0
		
elif (ssub == "Physics"):
	x = 1
			
elif (ssub == "Chemistry"):
	x = 2

elif (ssub == "Biology"):
	x = 3

elif (ssub == "Social_Science"):
	x = 4

else:
	print("enter valid input")

for i in database:
	if i == sname:
		print(sname,"scored",database[i][x])	

		



		 
                                                                               

 
