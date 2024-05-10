# Created By: Pranav Sure
# Created Date: 3/12/2024
# version = '1.0'
# -----------------------------------------------------
"""This file is a basic way for the user to interact and pick which ride they will be picking"""
# -----------------------------------------------------
# Built in Imports
# -----------------------------------------------------
# User Made Imports
# -----------------------------------------------------
print(
    """Welcome to Sriketh's Park, where fun doesn't exist.
      Here are the rides:
          1. Scenic River Cruise
          2. Carnival Carousel
          3. Jungle Adventure Water Splash
          4. Downhill Mountain Run
          5. The Regurgitator (Rollercoaster)
          6. 1984
          7. Lock In
          8. I didn't know what I was expecting
          9. Moon Bucks
          10. Let Me Finish
"""
)

ride_number = int(input("What ride would you like?(type the number): "))

# Check if the user wants the Scenic River Cruise(Ride 1)
if ride_number == 1:
    print(
        "You can go on the Scenic River Cruise\nStep right up for this wonderful ride called Scenic River Cruise. This cruise is a magical wonderland, with lush greenery and exquisite restaurants. You'll embark on a journey through the rapids in North Carolina to chilling on the beach in Thailand, you will experience luxury and paradise."
    )

elif ride_number >= 2 and ride_number <= 5:
    # Rest of rides

    # Ask age of rider(store it in variable rider_age)
    user_age = int(input("What is your age: "))

    # Check if the user wants the Carnival Carousel(Ride 2) and is in the age requirement(at least 3)
    if ride_number == 2 and user_age >= 3:
        print(
            "You can go on the Carnival Carousel\nThis is the Carnival Carousel. It is one of the largest carousel in the world, boasting a diameter of 200km wide. Go fast in this ride, with a speed of 500km/h and enjoy the ride. Take a sip of a drink from our exquisite bar."
        )

    # Check if the user wants the Jungle Adventure Water Splash(Ride 3) and is in the age requirement(at least 6)
    elif ride_number == 3 and user_age >= 6:
        print(
            "You can go on the Jungle Adventure Water Splash\nThis is the Jungle Adventure Water Splash. Jungle Adventure Water Splash, you will get catapulted into a jungle and must ride the river in a jetski to escape."
        )

    # Check if the user wants the Downhill Mountain Run(Ride 4) and is in the age requirement(at least 12)
    elif ride_number == 4 and user_age >= 12:
        print(
            "You can go on the Downhill Mountain Run\nThis ride has nothing else to it... It's just a ride that takes you down a mountain."
        )

    # Check if the user wants the The Regurgitator(Ride 5) and is in the age requirement(at least 12, but less than 70)
    elif ride_number == 5 and (user_age >= 12 and user_age <= 70):
        print(
            "You can go on the The Regurgitator\nThis is a stock standard rollercoaster. It has a cool name, but isn't cool at all"
        )
        # Check if the user wants the 1984(Ride 6) and is in the age requirement(at least 3)
    elif ride_number == 6 and user_age >= 3:
        print(
            "You can go on the 1984\nThis is the 1984, a carousel. It is one of the largest carousel in the world, boasting a diameter of 200km wide. Go fast in this ride, with a speed of 670 million mph and enjoy the ride to 1984. Take a sip of a drink from our exquisite bar."
        )

    # Check if the user wants the Lock-In(Ride 7) and is in the age requirement(at least 6)
    elif ride_number == 7 and user_age >= 6:
        print(
            "You can go on the Lock-In\nThis is an innovative escape room, where you have to 'Lock In' and figure out the code to unlock the safe. Then you'll have to grab the files and now have to hack and solve the code to get out.\n\nThe Twist?\n\n The safe is on a rollercoaster, and you have solve to make the rollercoaster stop.(Developed by Sid)"
        )

    # Check if the user wants the I didn't know what I was expecting(Ride 8) and is in the age requirement(at least 12)
    elif ride_number == 8 and user_age >= 12:
        print(
            "You can go on the I didn't know what I was expecting\nYou won't know what this ride is about, and to be honest we don't know either. Enter into the mysterious ride, where the ride changes every party. From catapulting jumps, to high speed carousels you won't know what's going to happen."
        )

    # Check if the user wants the Moon Bucks(Ride 9) and is in the age requirement(at least 12, but less than 70)
    elif ride_number == 9 and (user_age >= 12 and user_age <= 70):
        print(
            "You can go on the Moon Bucks\nMoon Bucks is an innovative ride as well as a restaurant, where instead of regular coffee, you get a moon-shaped coffee. It's amazing, and you will be transported to the moon with it's taste and the incredible height it reaches."
        )
        # Check if the user wants the Let Me Finish(Ride 10) and is in the age requirement(at least 12, but less than 70)
    elif ride_number == 10 and (user_age >= 12 and user_age <= 70):
        print(
            "You can go on the Let Me Finish\nFinishing is almost impossible, as this is a crazy hard escape room, where you have to solve countless problems, each exponentially harder than the last. You will need to get on a rollercoaster in the escape room, as well as countless other things like a floor drop and parachuting as well."
        )
    # this is to tell that if the user didn't pick a valid ride(or picked a ride in which he was to old)
    else:
        print("I'm sorry, you cannot go in. You don't meet the age requirement.")
else:
    print("Not a valid ride.")
