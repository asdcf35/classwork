import backend
import msvcrt
from rich.console import Console
def main():
    console = Console()
    restaurant_files = ['Burger City.csv', 'Bread Bitez.csv']
    restaurants = {}
    for restaurant_file in restaurant_files:
        restaurants[restaurant_file[:-4]] = backend.Restaurant(restaurant_file[:-4],True, restaurant_file)

    for index, restaurant in enumerate(restaurants.keys(), 1):
        print(f"{index}, {restaurant}")    

    restaurant_selected = list(restaurants.keys())[int(input("Select one of the restaurants(numbers only):\n")) - 1]
    restaurants[restaurant_selected].display_foods(console)
    console.print("\n\nEnter q to quit")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('ASCII')
            if key == "q":
                break
