import time

s1 = 50 
s2 = 50
calc = 0

vehicle_data={}

class Parking:
	def __init__(self,vh_no,entry,leave,vh_type,bill=0):
		self.vh_no = vh_no
		self.entry = entry
		self.leave = leave
		self.vh_type = vh_type
		self.bill = bill
		vehicle = Parking(vh_no,entery,leave,vh_type)

		vehicle_data[vh_no] = vehicle
	
	def getin(self):
		entry = time.time()
		vh_no = input("enter vehicle no:\n")
		vh_type = input("enter if it is  \
			1. 2 wheeler  \n  \
			2. 4 wheeler \n")

		if vh_type == 1:
			s1 -= s1

		elif vh_type == 2:
			s2 -= s2

		


	def getout(self):
		leave = time.time()
		vh_no = print("enter vehicle no: \n")
		
		calc = float(leave - entry)/3600
		
		if vh_type == 1:
			bill = calc*20

		elif vh_type == 2:
			bill = calc*30

	def slots(self):
		print("Slots remainig are \n\
			in 2 wheeler\n\
			in 4 wheeler\n",s1,s2)


print("Welcome to Parking \n\
	fare for 2 wheeler is 20/hr \n\
	fare for 4 wheeler is 30/hr\n")


while True:
	ch = int(input("Are you \
		1. Entering \n\
		2. Leaving"))

	if ch == 1:
		vehicle.getin()
		vehicle.slots()


	if ch ==2:
		vehicle.getout()
		vehicle.slots()

	# else:
	# 	break
