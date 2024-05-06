# Created By: Pranav Sure
# Created Date: 3/12/2024
# version = '1.0'
# -----------------------------------------------------
"""This file is a basic way for the user to interact and pick which ride they will be picking"""
# -----------------------------------------------------
# Built in Imports
import os
# -----------------------------------------------------
# User Made Imports
from modules.backend import Ride, rides_from_file
# -----------------------------------------------------

rides = rides_from_file('./init_files/rides.csv')
#IN_PROGRESS: list rides
all_rides = ""
for index, ride_name in enumerate(rides.keys()):
    all_rides += f"{index + 1}. {ride_name}\n"

#TODO: ask user(number or words)

#TODO: ask for age
#TODO: use age_check function(returns true if in the correct value, else False)
