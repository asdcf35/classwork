import rides
import concessions
import time
import os
import sys
from rich.progress import track
from random import *
import backend
import ropertor
if "idlelib" in sys.modules:
    print("The code will not work as intended.")
    quit()


#all of my pages
pages = [rides.main, concessions.main]


# Password setup
password = "123"
ride_operator_password = "ro123"
inputted = input("Enter Password(123 for regular, ro123 for ride operator console): ")

for step in track(range(0, 100, 5), "Checking Password..."):
    time.sleep(randint(100, 200) / 1000)


while True:
    if inputted in (password, ride_operator_password):
        break
    else:
        print("Sorry, not the correct password")
    if inputted == ride_operator_password:
        print("\n\nRide Operator Detected\n\n")
        for step in track(range(0, 100, 5), "Loading the Console..."):
            time.sleep(randint(100, 200) / 1000)
        ropertor.main()
        check_for_run = input("Do you want to check if the code fully runs?")
        if check_for_run == "y":
            print("Ok")
        else:
            print("Goodbye!")
            quit()
    while True:
        os.system('cls')
        print("Welcome to Sriketh's Park, where fun doesn't exist.")
        time.sleep(1)
        print("""
    Here are the options(select using the number):
        1. Rides
        2. Concessions  
        3. Water Park
    """)
        selection = input(
            "Select your option or q to quit. (numbers between 1 and 3)")
        selection = int(selection) if selection != "q" else 'q'
        if selection == "q":
            break
        try:
            pages[selection - 1]()
        except IndexError:
            print("Not a valid page, try again")
