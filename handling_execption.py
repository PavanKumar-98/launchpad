a = int(input("enter numeratotr"))
b = int(input("enter denominatotr"))
 
def div(x,y):
	res = float(x/y)


try:
	div(a,b)
	print(f"answer is{res}")

except ZeroDivisionError as err :
	print("division by zero!",err)











