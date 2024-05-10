from math import *
import sys
import subprocess
import os

os.system('py -m pip install pandas rich')
from rich.console import Console
import pandas as pd


def quit_no_input():
    """A q"""
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode("ASCII")
            if key == "q":
                break

# rides
class Ride:
    def __init__(self, name, age_range, desc, working) -> None:
        self.name = name
        self.age_range = age_range
        self.desc = desc
        self.working = working

    def check_age(self, age) -> bool:
        return self.age_range[0] < age < self.age_range[1]

    def working(self) -> None:
        self.working = not self.working


def rides_from_file(filename="rides.csv",admin=False) -> dict[str, Ride]:
    """
    Making Ride objects from a file

    Parameters
    ---
    filename : str, path object or file-like object
        the filename or object that you wish to use(must work with read_csv)
    """
    dataframex = pd.read_csv(filename)
    dataframex = dataframex.loc[dataframex["Working"] == True]
    dataframex.loc[:, "Max"] = dataframex.loc[:, "Max"].fillna(999999999)
    dataframex.loc[:, "Min"] = dataframex.loc[:, "Min"].fillna(0)
    dataframe = dataframex.to_dict("records")
    rides = {}
    for dictionary in dataframe:
        rides[dictionary["Name"]] = Ride(
            dictionary["Name"],
            (dictionary["Min"], dictionary["Max"]),
            dictionary["Description"],
            dictionary["Working"],
        )
    if admin == False:
        return rides
    else:
        return rides, dataframex


class Food_Item:
    def __init__(self, name, cost, available) -> None:
        self.name = name
        self.cost = cost
        self.available = available


class Restaurant:

    def __init__(self, name, open, filename) -> None:
        self.name = name
        self.open = open
        self.dataframe = pd.read_csv(filename)
        self.item_names = tuple(self.dataframe.loc[:, "Items"])
        self.items = [
            Food_Item(
                self.item_names[i],
                self.dataframe.loc[i, "Price"],
                self.dataframe.loc[i, "Available"],
            )
            for i in range(len(self.item_names))
        ]

    def display_foods(self, console: Console, discount=0) -> None:
        os.system("cls")
        console.print(f"Welcome to {self.name}\n\n", justify="center")
        console.print(f"Menu", justify="center")
        console.print(f'{"":-^30}', justify="center")
        print_half = self.dataframe.get(["Items", "Price"])
        console.print(print_half.to_string(index=False), justify="center")
