from multiprocessing import Value
import backend
import pandas as pd

import pandas


def main():
    # rides
    rides, dataframe = backend.rides_from_file("rides.csv", admin=True)
    list_of_rides = "Here is all the rides:\n"
    # add all the rides (formatted: <<Index Number>>. <<Ride Name>>)
    for index, ride_name in enumerate(rides.keys()):
        list_of_rides += f"\t{index + 1:>2}. {ride_name}\n"
    
    #print the string
    print(list_of_rides)

    #as the user which ride they want to edit
    user_ride = int(
        input(
            "Pick the ride you want to edit, or type q if you want to exit.(numbers only)\n"
        )
    )
    # set user_ride to the name of the ride(stored in the specific index of the keys of the rides)
    data_to_edit = dataframe.loc[dataframe["Name"] == list(rides.keys())[user_ride-1]]

    print("Options to change: ")
    print("\t1. Name - String")
    print("\t2. Min - Numbers")
    print("\t3. Max - Number")
    print("\t4. Description - Long String")
    print("\t5. Working - Boolean")

    #ask user to edit the format
    edit_format = int(input("What do you want to change(1 - 5): "))

    #ask the user for the final amount
    change = input("What are you changing it to: ")

    #if they want to edit the name, change the name
    if edit_format == 1:
        data_to_edit["Name"] = change
    
    #check if they want to edit the min age
    elif edit_format == 2:
        #check if the integer is an input
        try:
            change = int(change)
        
        #if the value error is not a valid input
        except ValueError:
            print("Sorry, not a valid input")
        
        #update the change
        else:
            data_to_edit["Min"] = change
    
    #check if they want to edit the min age
    elif edit_format == 3:
        #check if the integer is an input
        try:
            change = int(change)

        #if the value error is not a valid input
        except ValueError:
            print("Sorry, not a valid input")
        
        #update the change
        else:
            data_to_edit["Max"] = change
    
    #check if they want to edit the description
    elif edit_format == 4:
        data_to_edit["Description"] = change
    
    #check if the ride is working
    elif edit_format == 5:
        #check if the change is not in true or false
        if change.lower() not in ("true", "false"):
            print("Sorry, not a valid input")
        
        #change it to true or false depending on the answer
        else:
            change = False if change.lower() == "false" else True
            data_to_edit["Working"] = change

    #change the full code
    dataframe.loc[dataframe['Name'] == list(rides.keys())[user_ride]] = data_to_edit
    
    #print the edited csv
    print("Here is that data:", dataframe, sep="\n")

    #print the rides
    dataframe.to_csv("rides.csv")


if __name__ == "__main__":
    main()
