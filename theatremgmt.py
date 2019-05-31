import json
import csv

seatsReq = 0
movie = []
currentData = []
ticketPrice = 0

def openUpcomingMovies():
	upcomingData = getJsonData("upcomingMovies.json")
 	for idd, results in enumerate(upcomingData):
		print "{} {}\n".format(idd,results["name"])
	movieNum = int(input("\nEnter the movie number: \n"))
	if movieNum > idd:
		print "\nEnter correct movie number\n"
	else:
		upcomingMovie = upcomingData[movieNum] 
		print "\nMovie Name: {}".format(upcomingMovie['name'])
		print "\nDescription: {}".format(upcomingMovie['description'])
		print "\nCast: {}".format(upcomingMovie['cast'])
		print "\nRelease time: {}".format(upcomingMovie['release'])
	upcomingMovies()

def upcomingMovies():
	ans = raw_input("\nLooking for upcoming movies?\tYes or No\n\n")
	if ans == "Yes" or ans == "yes":
		openUpcomingMovies()
	else:
		ans = raw_input("\nDo you want to book movies?\tYes or No\n\n")
		if ans == "Yes" or ans == "yes":
			main()
		else:			
			print "\n---THANK YOU FOR CHOOSING ABC CINEMAS---"
			exit()

def updateJson():
	defaultSeat = movie['seats'] - seatsReq
	movie['seats'] = defaultSeat 
	with open("currentMovies.json","w") as f:
		json.dump(currentData,f)
	inFile = open("currentMovies.json","r")
	outFile = open("currentData.csv","w")
	writer = csv.writer(outFile)
	count = 0
	for row in json.loads(inFile.read()):
		if count == 0:
			header = row.keys()
			writer.writerow(header)
			count += 1
		writer.writerow(row.values())
	return 1	

def printTicket():
	print "\nHere is your ticket:"
	print "\nMovie Name: {}".format(movie['name'])
	print "\nShow Time: {}".format(movie['timings'])
	print "\nNumber of seats booked: {}".format(seatsReq)
	print "\nTotal Amount: {} INR".format(ticketPrice)
	print "\nSTATUS ---> BOOKED\n"
	update = updateJson()
	upcomingMovies()

def confirmBooking():
	ans = raw_input("\nAre you SURE?\tYes or No\n\n")
	printTicket() if ans == "Yes" or ans == "yes" else gotoStart()
		
def payForTicket():
	ans = raw_input("\nProceed to payment?\tYes or No\n\n")
	if ans == "Yes" or ans == "yes":
		confirmBooking()
	else:
		ans = raw_input("\nCancel the plan?\tYes or No\n\n")
		gotoStart() if ans == 1 else checkOut()
			
def gotoStart():
	ans = raw_input("\nWish to continue?\tYes or No\n\n")
	displayMovies() if ans == "Yes" or ans == "yes" else  "\n---THANK YOU FOR VISITING ABC CINEMAS---"
		
def checkOut():
	print"\nSelect Class:\n"
	print "\n1.First Class: {} INR".format(movie['first'])
	print "\n2.Second Class: {} INR".format(movie['second'])
	print "\n3.Third Class: {} INR".format(movie['third'])
	getClass = int(input("\nWhich class?\n"))
	global ticketPrice
	if getClass == 1:
		print "\n!!Great!!\n"
		ticketPrice = movie['first'] * seatsReq
		print "Total Ticket Price --> {} INR".format(ticketPrice)
	elif getClass == 2:
		print "\n!!Superb!!\n"
		ticketPrice = movie['second'] * seatsReq
		print "Total Ticket Price --> {} INR".format(ticketPrice)
	else:
		print "\n!!Good!!\n"
		ticketPrice = movie['third'] * seatsReq
		print "\nTotal Ticket Price --> {} INR".format(ticketPrice)
	payForTicket()

def startBooking():
	print "\nMovie Name: {}".format(movie['name'])
	print "\nShow Time: {}".format(movie['timings'])
	print "\nAvailable Seats: {}".format(movie['seats'])
	global seatsReq
	seatsReq = int(input("\nEnter the number of seats: \n"))
	noOfSeat = movie['seats']
	if seatsReq <= noOfSeat:
		checkOut()
	else:
		print "\n  Sorry no tickets available\n" 
		gotoStart()
		
def displayShowDetails():
	print "\nMovie Name: {}".format(movie['name'])
	print "\nDescription: {}".format(movie['description'])
	print "\nScreen: {}".format(movie['screen'])
	print "\nShow Time: {}".format(movie['timings'])
	print "\nAvailable Seats: {}".format(movie['seats'])
	ans = raw_input("\nWish to book tickets?\tYes or No\n\n")
	startBooking() if ans == "Yes" or ans == "yes" else gotoStart()	
	
def getJsonData(fileName):
	with open(fileName,'r') as f:
  		json_currentData = f.read()
  	obj = json.loads(json_currentData)
  	return obj

def displayMovies():
	print "\n--MOVIES RUNNING NOW--\n"
	global currentData
	currentData = getJsonData('currentMovies.json')
	for idd, results in enumerate(currentData):
		print " {} {}\n".format(idd,results["name"])
	ans = raw_input("Do you want to book?\tYes or No\n\n")
	if ans == "Yes" or ans =="yes":
	 	movieNum = int(input("\nEnter the movie number: \n\n"))
	 	if movieNum > idd:
	 		print "\nEnter correct movie number"
	 		upcomingMovies()
		else:
			global movie
			movie = currentData[movieNum]
			displayShowDetails()

def main():
	print "Welmoviecome to ABC Cinemas"
	displayMovies()	

if __name__ == '__main__':
	main()