database = { "Steve": [78, 87 ,98, 88, 79], "Martin":[45, 99, 100, 89, 88], "Trish" :[66, 68 ,70 ,71, 68]}
database["Alex"] =[50 ,98, 69, 78, 89]
new = {}
Math = 0
Physics = 1
Chemistry = 2
Biology = 3
Social_Science = 4
x=0
# while True:
# 	name = input("enter the name \n")
# 	subject = input("enter the subject with spaces\n")
# 	if name == "":
# 		break

# 	marks = list(subject.split())
# 	database[name] = marks

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

# else:
# 	print("enter valid input")
for i in database:
	new[i] = database[i][x]


final = list(sorted(new.items(), key = lambda kv:(kv[1], kv[0]),reverse = True))
print(final)


