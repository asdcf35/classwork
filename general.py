# created by : Prasant Neupane
# date created : 5/6/24 10:50
# version = '1.0'
#-------------------------
""" This code is a simple way to tell the user all the rules and the operating hours of the themepark """
#-------------------------
# Built in Imports
import time
from ride.console import Console
#-------------------------
# User made Imports
#-------------------------


def rules():
    """prints the rules of the themepark and brings user back to main page if user chooses to """
    while True:
        print("""Here are the main rules in the theme park:
1. No running or jogging within the park premises.
2. Dispose of all trash in designated bins; only throw food waste in trash receptacles.
3. Keep hands, arms, legs, and feet inside the rides at all times.
4. Maintain appropriate behavior; refrain from making out on rides (hotel accommodations are available).
5. Cell phone usage is prohibited while on rides.
6. Guests under the age of 3 are not permitted on any rides.
7. Guests with heart conditions or related health issues should refrain from participating in park activities.
8. Guests older than 80 years old are not permitted to engage in rides or attractions.
9. Individuals prone to motion sickness or dizziness should avoid participating in certain rides.
10. Pregnant guests are not allowed to partake in park activities.""")
        
        #ask user if they want to go back
        quit2 = input('Do you want to go back? (y/n): ')

        #if they do, break the loop
        if quit2.lower() == 'y':
            break
        #if they don't quit the whole program
        elif quit2.lower() == 'n':
            quit()
        else:
            print("Input is invalid, try again")


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
        
        #if the user types 'y', goes back to general
        if quit2.lower() != 'n':
            break

def main():
    #create console times
    console = Console()
    while True:
        try:
            #ask user if they want to go to rules or park hours
            chosen = int(
                input('Do you want to:\n1. Read the rules of park\n2. Check the park hours\n3. Go back to the main page:\n'))

            #if user inputs 1, go to rules
            if chosen == 1:
                print("Going to rules...")
                time.sleep(1)
                rules(console)

            #if user inputs 2, go to park_hours
            elif chosen == 2:
                print("Going to park hours...")
                time.sleep(1)
                hours(console)
            
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