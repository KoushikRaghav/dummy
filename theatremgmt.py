import json
import csv

seatsReq = 0
movie = []
currentData = []
ticketPrice = 0
showTimeSeats = []

def checkForAns(ans):
	answer = ans.lower()
	if answer =="yes":
		return 1
	elif answer == "no":
		return 0
	else:
		print "\nEnter Yes or No\n"
		main()

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
	if (checkForAns(ans)):
		openUpcomingMovies()
	else:
		ans = raw_input("\nDo you want to book movies?\tYes or No\n\n")
		if (checkForAns(ans)):
			main()
		else:			
			print "\n---THANK YOU FOR CHOOSING ABC CINEMAS---"
			exit()

def updateJson():
	defaultSeat = showTimeSeats["AvailableSeats"] - seatsReq
	showTimeSeats["AvailableSeats"] = defaultSeat 
	print showTimeSeats["AvailableSeats"]
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
	
def printTicket():
	print "\nHere is your ticket:"
	print "\nMovie Name: {}".format(movie['name'])
	print "\nShow Time: {}".format(json.dumps(showTimeSeats["AvailableSeats"]))
	print "\nNumber of seats booked: {}".format(seatsReq)
	print "\nTotal Amount: {} INR".format(ticketPrice)
	print "\nSTATUS ---> BOOKED\n"
	updateJson()
	upcomingMovies()

def confirmBooking():
	ans = raw_input("\nAre you SURE?\tYes or No\n\n")
	printTicket() if (checkForAns(ans)) else gotoStart()
		
def payForTicket():
	ans = raw_input("\nProceed to payment?\tYes or No\n\n")
	if (checkForAns(ans)):
		confirmBooking()
	else:
		ans = raw_input("\nCancel the plan?\tYes or No\n\n")
		gotoStart() if (checkForAns(ans)) else checkOut()
			
def gotoStart():
	ans = raw_input("\nWish to continue?\tYes or No\n\n")
	displayMovies() if (checkForAns(ans)) else  "\n---THANK YOU FOR VISITING ABC CINEMAS---"

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

def checkForSeats(noOfSeat):
	if seatsReq <= noOfSeat:
		checkOut()
	else:
		print "\n  Sorry no tickets available\n" 
		gotoStart()

def startBooking(ans):
	global seatsReq
	global showTimeSeats
	showTimeSeats = movie['showDetails'][ans]
	print "\nMovie Name: {}".format(movie['name'])
	print "\nShow Time: {}".format(json.dumps(showTimeSeats["ShowTime"]))
	print "\nAvailableSeats: {}".format(json.dumps(showTimeSeats["AvailableSeats"]))
	seatsReq = int(input("\nEnter the number of seats: \n"))
	noOfSeat = json.dumps(showTimeSeats["AvailableSeats"])
	checkForSeats(noOfSeat)
			
def displayShowDetails():
	print "\nMovie Name: {}".format(movie['name'])
	print "\nDescription: {}".format(movie['description'])
	print "\nScreen: {}".format(movie['screen'])
	for showNum in movie["showDetails"]:
		print "\n<-- {} -->".format(json.dumps(showNum))	
	ans = int(input("\nEnter show\t0 or 1?\n\n"))
	startBooking(ans) if (ans <= 1) else gotoStart()	
	
def getJsonData(fileName):
	with open(fileName,'r') as f:
  		json_currentData = f.read()
  	obj = json.loads(json_currentData)
  	return obj

def initiateBooking(ans,movieSNum):
	if (checkForAns(ans)):
	 	movieNum = int(input("\nEnter the movie number: \n\n"))
	 	if movieNum > movieSNum:
	 		print "\nEnter correct movie number"
	 		upcomingMovies()
		else:
			global movie
			movie = currentData[movieNum]
			displayShowDetails()
	
def displayMovies():
	print "\n--MOVIES RUNNING NOW--\n"
	global currentData
	currentData = getJsonData('currentMovies.json')
	for movieSNum, results in enumerate(currentData):
		print " {} {}\n".format(movieSNum,results["name"])
	ans = raw_input("Do you want to book?\tYes or No\n\n")
	return ans,movieSNum
	
def main():
	print "Welcome to ABC Cinemas"
	ans, movieSNum = displayMovies()
	initiateBooking(ans,movieSNum)
	
if __name__ == '__main__':
	main()
