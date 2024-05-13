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
password_inputted = ""
#check passcodes

## actual main code