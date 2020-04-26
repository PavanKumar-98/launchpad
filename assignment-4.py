import string



string1 = []
string2 = []

def correction(x):
	res = ""
	for char in x:
		
		if char not in string.digits:
			if char not in string.punctuation:
				res = res + char
				return(string2.append(res))



string1 = input("\nenter the strings")

for i in (string1):
	correction(i)

print("".join(string2))
	






