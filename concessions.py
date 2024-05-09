import backend
import msvcrt
from rich.console import Console
import os

def main():
    while True:
        os.system('cls')
        console = Console()

        restaurant_files = ["Burger City.csv", "Bread Bitez.csv"]
        restaurants = {}
        for restaurant_file in restaurant_files:
            restaurants[restaurant_file[:-4]] = backend.Restaurant(restaurant_file[:-4], True, restaurant_file)

        print("Here is all the restaurants we have:")
        for index, restaurant in enumerate(restaurants.keys(), 1):
            print(f"{index}. {restaurant}")
        number = input("Enter one of the restaurants(number only), or q to quit")
        number = "q" if number == "q" else int(number) - 1
        if number == "q":
            break
        try:
            restaurant_selected = list(restaurants.keys())[number]
        except ValueError:
            print("The value is invalid, please try again.")
        else:
            restaurants[restaurant_selected].display_foods(console)
            console.print("\n\nEnter q to go back to the restaurants", justify="center")
            backend.quit_no_input()
