# created by : Pranav Sure
# date created : 5/10/24
# version = '1.0'
#-------------------------
""" This code is a simple way to tell the user all the rules and the operating hours of the themepark """
#-------------------------
# Built in Imports
import time
import datetime.time as t
from ride.console import Console
#-------------------------
# User made Imports
import backend
#-------------------------


def rules(console):
    """prints the rules of the themepark and brings user back to main page if user chooses to """
    console.print("""Here are the main rules in the theme park:
1. No running or jogging within the park premises.
2. Dispose of all trash in designated bins; only throw food waste in trash cans.
3. Keep hands, arms, legs, and feet inside the rides at all times.
4. Maintain appropriate behavior; refrain from making out on rides (hotel accommodations are available).
5. Cell phone usage is prohibited while on rides.
6. Guests under the age of 3 are not permitted on any rides.
7. Guests with heart conditions or related health issues should refrain from participating in park activities.
8. Guests older than 80 years old are not permitted to engage in rides or attractions.
9. Individuals prone to motion sickness or dizziness should avoid participating in certain rides.
10. Pregnant guests are not allowed to partake in park activities.""", justify="center")
    
    #print that q must be pressed in order to exit
    console.print("Enter q to go back to the general park info page.", style='green',justify='center')

    #quit with no input, and i don't even need to loop as the user can press any key he wants, and the thing will not work until q has been pressed
    backend.quit_no_input()

def hours(console):
    """Prints hours of the park, and finds if it open or not"""
    opening_time = t.time(hour=11, minute=0)
    closing_time = t.time(hour=20, minute=0)
    while True:
        #print the opening times, and if it open or not
        console.print(f"The opening times of the park are from 11am to 8pm everyday. Right now it is {'open' if opening_time < t.now() and t.now() < closing_time else 'closed'}",justify='center')
        
        console.print("Enter q to go back to the general park info page.", style='green',justify='center')

        #quit with no input, and i don't even need to loop as the user can press any key he wants, and the thing will not work until q has been pressed
        backend.quit_no_input()


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
                rules(console)

            #if user inputs 2, go to park_hours
            elif chosen == 2:
                hours(console)
            
            #if the user chooses 3, quit to the main page
            elif chosen == 3:
                break

            #if any other number, raise a ValueError(because that's an invalid number)
            else:
                raise ValueError

        except ValueError:
            print("Invalid choice, try again")