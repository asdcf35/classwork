# Created By: Pranav Sure
# Created Date: 5/10/2024
# version = '1.0'
# -----------------------------------------------------
"""This file is a basic way for the user(and ride operator) to interact and pick where they will be going"""
# -----------------------------------------------------
# Built in Imports
import time
import datetime
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

#this is meant to be used in IDLE


## password code

#stored password
customer_password = "123"
ride_operator_password = "r123"
#ask for password

password_inputted = input("Input '123' to explore the park, or input 'r123' to check on the status of the rides")
#progress bar as wait



#if user inputted customer password -> let him in regular
if password_inputted == customer_password:
    print("Welcome to Sriketh's Park, where fun doesn't exist.")
else:
    print("")
## actual main code