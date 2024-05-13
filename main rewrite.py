# Created By: Pranav Sure
# Created Date: 5/10/2024
# version = '1.0'
# -----------------------------------------------------
"""This file is a basic way for the user(and ride operator) to interact and pick where they will be going"""
# -----------------------------------------------------
# Built in Imports
import time
import os
import sys
from random import *
# -----------------------------------------------------
# User Made Imports and 3rd party imports
import rides
import concessions
import roperator
from rich.progress import track
# -----------------------------------------------------

#NOTE: This code is meant to run in a terminal, it has not been tested in IDLE.

#checks if it is running in IDLE
if "idlelib" in sys.modules:
    print("The code will not work as intended.")
    quit()




#Create list named main storing all the functions(pages)
pages = [rides.main, concessions.main]

# the passwords
password = "123"
ride_operator_password = "ro123"

#Ask user for password
password_inputted = input(
    "Enter Password(123 for regular, ro123 for ride operator console): ")


#this is analogous to a sleep function, looks cooler(imho)
for step in track(range(0, 100, 5), "Checking Password..."):
    time.sleep(randint(100, 200) / 1000)

#check if the password is either the passwod or the ride operator password
if password_inputted in (password, ride_operator_password):

    #check if the password is the ride operator password
    if password_inputted == ride_operator_password:
        print("\n\nRide Operator Detected\n\n")

        #similar to a sleep function(but looks cooler imho)
        for step in track(range(0, 100, 5), "Loading the Console..."):
            time.sleep(randint(100, 200) / 1000)

        #call the ride operator page
        roperator.main()

        #after, check if they want to see if the code fully runs
        check_for_run = input(
            "Do you want to check if the code fully runs?('y' for yes, anything else for no)"
        )
        #if yes('y'), continue onto the actual code
        if check_for_run == "y":
            print("Ok")
        #else(anything else) -> print goodbye and exit code
        else:
            print("Goodbye!")
            quit()

    #the main code(either from accepting changes from the ride operator, or not actually written)
    while True:
        #clear the system
        os.system('cls')

        #greet them(this is on purpose, plus I have spoken confirmation from Sriketh Boyina)
        print("Welcome to Sriketh's Park, where fun doesn't exist.")
        #sleep
        time.sleep(1)

        #the options
        print("""
    Here are the options(select using the number):
        1. Rides
        2. Concessions  
    """)

        #ask the user for numbers
        selection = input(
            "Select your option or q to quit. (numbers between 1 and 2)")
        try:
            #if not q, try to change selection to an integer, otherwise keep it
            selection = int(selection) if selection != "q" else 'q'

        #if it can't be turned into an integer, then catch the erro and replace it with a invalid value to the person
        except ValueError:
            print("Sorry, the value is invalid")
        else:
            #if it is q, then exit the code
            if selection == "q":
                break
            #try and index the pages using the pages system
            try:
                pages[selection - 1]()
            #if indexerror(when the people put a number higher than 1)
            except IndexError:
                print("Not a valid page, try again")

#if the password is not the password or the ride operator password, then print the following
else:
    print("Sorry, not the correct password")