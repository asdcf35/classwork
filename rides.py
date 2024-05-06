# Created By: Pranav Sure
# Created Date: 3/12/2024
# version = '1.0'
# -----------------------------------------------------
"""This file is a basic way for the user to interact and pick which ride they will be picking"""
# -----------------------------------------------------
# Built in Imports
import os
from time import sleep
from math import inf
import colorama
# -----------------------------------------------------
# User Made Imports
from modules.backend import Ride, rides_from_file

# -----------------------------------------------------
# create Ride objects from all the list objectas
rides = rides_from_file("./init_files/rides.csv")

#create variable holding list of all rides
list_of_rides = "Here is a list of all the rides:\n"
#add all the rides (formatted: <<Index Number>>. <<Ride Name>>)
for index, ride_name in enumerate(rides.keys()):
    list_of_rides += f"\t{index + 1}. {ride_name}\n"

#Print all the rides
print("Welcome to the Amusement Park!")
sleep(1)
print(list_of_rides)

def disp_ride(ride: Ride) -> None:
    """
    Displays the ride in a presentable way

    Parameters:
    ride : the current ride that is being used
    """
    os.system("clear")
    
    
#ask user(numbers)
try:
    #ask the user which ride they want to go to
    user_ride = input("Pick the ride you want to go on, or type q if you want to exit.(numbers only)\n")
    #if the user enters q(exit value), exit
    if user_ride == 'q':
        print("Thank you for visiting the Amusement Park! Here's a gift for you!")
        #TODO: a pdf or html of them taking a picture with the camera
    else:
        #set user_ride to the name of the ride(stored in the specific index of the keys of the rides)
        user_ride = list(rides.keys())[int(user_ride)-1]
except ValueError:
    print("Input is invalid. Please try again.")
else:
    # check if there is any age restrictions(if it is not 0 and inf)
    if rides[user_ride].age_range == (0, inf):
        disp_ride()
    print(f"The {rides[user_ride]} is a great choice! However we need to check your age.")
    age = input("What is your age? ")
    # TODO: use age_check function(returns true if in the correct value, else False
    if rides[user_ride].check_age:
        print(rides[user_ride].desc)
    else:
        print("Sorry we can't let you go in.")