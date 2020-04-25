mydict = {"hello" : "world", "speckbit" : "self-learning", "life" : "meaning"}
a = input("enter the string to search")
for i in mydict:
	if mydict[i] == a:
		print(i)