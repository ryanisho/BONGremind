from twilio.rest import Client
from datetime import datetime
from twilio.twiml.voice_response import VoiceResponse, Say
import datetime
import time
import os

account_sid = 'SID_TOKEN'
auth_token = 'AUTH_TOKEN'
client = Client(account_sid, auth_token)


affirmative_answers = ["Yes", "Y", "yes", "y"]
negative_answers = ["No", "no", "N", "n"]


#Misc
currentDT = datetime.datetime.now()
currentDT.strftime("%I:%M:%S %p")
current_date = currentDT.strftime("%a, %b %d, %Y")
current_time = currentDT.strftime("%I:%M:%S %p")

def sleeper():
		num = input("How many seconds would you like me to wait?\n")
		print(" ")

		try:
			num = int(num) 
		except ValueError:
			print("Please enter a valid time unit. \n")

		print(f'Waiting {num} second(s).')
		time.sleep(num)

os.system('cls') #This is the clear screen operation for Windows

while True:
	print("\t**********************************************")
	print("\t** Welcome to Text-Remind: A simple web app **")
	print("\t**********************************************")
	print(f"Today's date is: {current_date}.")
	print(f"The current time is: {current_time}.")
	key = input("Please enter the authentication key.\n")
	if key == 'Windows8.1':
		print(" ")
		print("Key validated.")
		print(" ")
		print("Welcome back Ryan!")
		break
	elif key == 'Guest':
		print("Key validated.")
		print("You are a guest user.")
		break
	else:
		print("Incorrect Key. Try again.")

print(f"This program is currently still in Beta Development.")

phone_number = input("Enter the target phone number. +1[AC][F3][L4]\n")

while True:
	print(" ")
	text = input("What's the reminder?\n")

	try:
		sleeper()
	except KeyboardInterrupt:
		print('\n\nKeyboard exception recieved. Exiting.')
		exit()

	message = client.messages \
	    .create(
	         body=text,
	         to=phone_number,
	         from_='+16097335940'
	     )

	call = client.calls.create(
	                twiml='<Response><Say>This is the automated timer notification call!Say></Response>',
	                to=phone_number,
	                from_='+16097335940'
	            )

	try_again = input("Would you like to set another reminder? (Y/N) \n")
	if try_again in negative_answers:
		print("Exception recieved. Exiting")
		break 
	else: 
		print("")
