import rides
import concessions
import water_park
import time
import os
import sys
from rich.progress import track
from random import *
if "idlelib" in sys.modules:
    print("The code will not work as intended.")
    quit()




pages = [rides.main, concessions.main, water_park.main]


def homepage():
    print("Welcome to Sriketh's Park, where fun doesn't exist.")
    time.sleep(1)
    print("""
Here are the options(select using the number):
    1. Rides
    2. Concessions  
    3. Water Park
""")

# Password setup
password = "password"
inputted = input("Enter Password")
for step in track(range(100),"Processing..."):
    time.sleep(randint(100, 200)/1000)

while True:
    try:
        os.system('cls')
        homepage()
        selection = input(
            "Select your option or q to quit. (numbers between 1 and 3)")
        selection = int(selection) if selection != "q" else 'q'
    except ValueError:
        print(
            "Sorry! Invalid Input. Make sure you are only using numbers and not any other characters."
        )
    else:
        if selection == "q":
            break
        try:
            pages[selection - 1]()
        except IndexError:
            print("Not a valid page, try again")
