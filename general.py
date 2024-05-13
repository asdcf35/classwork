# created by : Prasant Neupane
# date created : 5/6/24 10:50
# version = '1.0'
#-------------------------
""" This code is a simple way to tell the user all the rules and the operating hours of the themepark """
#-------------------------
# Built in Imports
import time
from ride.console import Console()
#-------------------------
# User made Imports
#-------------------------


def rules():
    """prints the rules of the themepark and brings user back to main page if user chooses to """
    while True:
        print("""Here are the main rules in the theme park:
            1. No sprinting
            2. No littering/only throw food in the trash
            3. Kee p hands, arms, legs, and feet inside the rides at all times
            4. No making out on the rides (Why would you do that? We have hotels available)
            5. Don't use cell phones on rides
            6. No one younger than 3 on any rides
            7. No one with health issues concerning heart issues
            8. No one older than 80 years old
            9. No motion sickness or dizziness
            10. No pregnant mothers""")

        quit2 = input('Do you want to go back to the main page? (y/n): ')

        if quit2.lower() != 'n':
            break


def hours():
    """Prints hours of the park, and finds if it open or not"""
    while True:
        print("""
        Here are the operating hours for the theme park:
        Saturday: 5:00 AM to 11:59 PM
        Sunday: 5:00 AM to 11:59 PM
        Monday to Thursday: 6:00 AM to 11:59 PM
        Friday: 6:00 AM to 11:59 PM
            """)
        
        #ask the user if they want to go back to the page 
        quit2 = input('Do you want to go back? (y/n): ')
        
        #if the user types 'n', goes back to general
        if quit2.lower() != 'n':
            break

def main():
    while True:
        try:
            #ask user if they want to go to rules or park hours
            chosen = int(
                input('Do you want to:\n1. Read the rules of park\n2. Check the park hours\n3. Go back to the main page:\n'))

            #if user inputs 1, go to rules
            if chosen == 1:
                print("Going to rules...")
                time.sleep(1)
                rules()

            #if user inputs 2, go to park_hours
            elif chosen == 2:
                print("Going to park hours...")
                time.sleep(1)
                hours()
            
            #if the user chooses 3, quit to the main page
            elif chosen == 3:
                break

            #if any other number, raise a ValueError(because that's an invalid number)
            else:
                raise ValueError

        except ValueError:
            print("Invalid choice.")
            print("please try again")
            time.sleep(1)