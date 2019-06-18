numb = 0
vehData = []
floorList = []
vehicleType = 0
numOfFloors = 2
parkingData = []
vehicleData = []
vehicleNumber = []
vehicleList = []

class Parking:
	def __init__(self,VE=None):
		# ,bike=None,bus=None,van=None):
		self.veh = VE
		# self.bike = bike
		# self.bus = bus
		# self.van = van

	def getTotalVehicles(self):
		return (self.veh)

class Vehicle:
	def __init__(self,vType,vNumber,floor):
		self.VType = vType
		self.VNumber = vNumber
		self.VFloor = floor

	def getFloor(self):
		return self.VFloor

	def getVTtype(self):
		return self.VType

	def getNumber(self):
		return self.VNumber

def unparkVehicle():
	print "\n<--- VEHICLE UNPARKING --->"
	getVehNum = int(input("\nEnter your vehicle number: "))
	if getVehNum in vehicleNumber:
		print "\nYour vehicle is found"
		for unPark in vehData:
			print "\n\tFloor: {}".format(unPark.getFloor())
			print "\n\tVehicle Type: {}".format(vehicleList[unPark.getVTtype()])
			print "\n\tVehicle Number: {}".format(unPark.getNumber())
			print "\n\t!!! UNPARKED !!!"
			if unPark.getVTtype() == 0:
				floorList.veh += 1
				print floorList.veh
			# elif unPark.getVTtype() == 1:
			# 	floorList.bike += 1
			# elif unPark.getVTtype() == 2:
			# 	floorList.bus += 1
			# elif unPark.getVTtype() == 3:
			# 	floorList.van += 1		
	else:
		print "\nYour vehicle is not found"

def parkVehicle(floor):
	global floorList,vehicleData,vehData
	floorList = parkingData[floor]
	vehicleData = Vehicle(vehicleType,numb,floor)
	vehData.append(vehicleData)
	#for vehicleList[vehicleType] in vehicleList:

	if vehicleType == 0 or vehicleType == 1:
		#a = (', '.join(vehicleList[vehicleType]))
		#halo = vehicleList[vehicleType](', '.join(vehicleList))
		#import pdb;pdb.set_trace()
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		print "\n\tFloor: {}".format(vehicleData.getFloor())
		if floorList.veh != 1:
			floorList.veh -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorList.veh)
			print "{}".format(floorList.getTotalVehicles())
	# elif vehicleType == 1:
	# 	print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
	# 	print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
	# 	print "\n\tFloor: {}".format(vehicleData.getFloor())
	# 	if floorList.bike != 0:
	# 		floorList.bike -= 1
	# 		print "\n\t!!! PARKED !!!"
	# 		print "{}".format(floorList.bike)
	# 		print "{}".format(floorList.getTotalVehicles())
	# elif vehicleType == 2:
	# 	print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
	# 	print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
	# 	print "\n\tFloor: {}".format(vehicleData.getFloor())
	# 	if floorList.bus != 0:
	# 		floorList.bus -= 1
	# 		print "\n\t!!! PARKED !!!"
	# 		print "{}".format(floorList.bus)
	# 		print "{}".format(floorList.getTotalVehicles())
	# elif vehicleType == 3:
	# 	print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
	# 	print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
	# 	print "\n\tFloor: {}".format(vehicleData.getFloor())	
	# 	if floorList.van != 0:
	# 		floorList.van -= 1
	# 		print "\n\t!!! PARKED !!!"
	# 		print "{}".format(floorList.van)
	# 		print "{}".format(floorList.getTotalVehicles())

def searchFloors():
	if vehicleType == 0 or vehicleType == 1 or vehicleType == 2 or vehicleType == 3:
		print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
		for vehiclee in parkingData:
			print "Floor {} --> AVAILABLE\n\t".format(parkingData.index(vehiclee)) if vehiclee.veh > 0 else "\t"
		floor = int(input("Enter the floorNum: "))
		return floor

def checkForAvailability():
	return True if vehicleType < len(vehicleList) else False

def checkVehicleNumber(numb):
	count = 0
	while numb > 0:
		numb = numb // 10
    	count += 1
	return True if count == 4 else False	

def getVehicleData():
	global numb,vehicleType
	print "\n<--- VEHICLE PARKING --->"
	vehicleType = int(input("\nEnter Vehicle Type: \n\n0. Car\t1. Bike\t2. Bus\t3. Van\n\n"))
	if vehicleType <= 3:
		numb = int(input("\nEnter Vehicle Number: "))
		return 1 if checkVehicleNumber(numb) == True  else 0	
	else:
		print "Enter the vehicle type correctly"

def displayVehicleData():
	print "_-"*23
	print "\nFloor\tCars\tBikes\tBuses\tVans\tTotal"
	print "_-"*23
	for vehicles in parkingData:
		print "\n {}\t {}\t {}\t {}\t {}\t  {}\n".format(parkingData.index(vehicles),vehicles.car,vehicles.bike,vehicles.bus,vehicles.van,vehicles.getTotalVehicles())

def enterVehicleData():
	global parkingData,numOfFloors
	print "\n<--- ENTER VEHICLE DATA --->"
	for numOfFloors in range(2):
		print "\n    --- Floor {} ---".format(numOfFloors)
		vehicleLimit = int(input("\nEnter the number of vehicles: "))
		car = int(input("\n\tCar(s): "))
		newData = Parking(car)
		totalVehicles = newData.getTotalVehicles()
		if totalVehicles == vehicleLimit:
			parkingData.append(newData)
			print "\nDATA STORED SUCCESSFULLY"
		else:
			print "\nEnter vehicles count within {}\n".format(vehicleLimit)
			break

def getMenuOption():
	option = int(input("1. Enter Data\n2. Park my vehicle\n3. Unpark my vehicle\n4. Display Availability\n5. Exit\n\n"))
	return option

def main():
	vehicleList.append(Parking("Car"))
	vehicleList.append(Parking("Bike"))
	vehicleList.append(Parking("Bus"))
	vehicleList.append(Parking("Van"))
	print vehicleList[1].veh
	global vehicleNumber,numOfFloors
	while 1:
		print "\n<--- PARKING SYSTEM --->\n"
		option = getMenuOption()
		if option == 1:
			enterVehicleData()		
		elif option == 2:
			VData = getVehicleData()
			vehicleNumber.append(numb)		
			check = checkForAvailability()
			floor = searchFloors() if check == True else "\nEnter Correct Vehicle Type\n"
			parkVehicle(floor) if floor <= numOfFloors else "\nPARKING IS FULL IN FLOOR {}".format(floor)
		elif option == 3:
			unparkVehicle()
		elif option == 4:
			displayVehicleData()
		elif option >= 5 or option == 0:
			print "BYE"
			exit()
	
if __name__ == '__main__':						
	main()