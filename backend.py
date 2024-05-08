from math import *
import sys
import subprocess
import os

from rich.console import Console
import pandas as pd

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


def rides_from_file(filename="rides.csv") -> dict[str, Ride]:
    """
    Making Ride objects from a file

    Parameters
    ---
    filename : str, path object or file-like object
        the filename or object that you wish to use(must work with read_csv)
    """
    dataframe = pd.read_csv(filename)
    dataframe.loc[:, "Max"] = dataframe.loc[:, "Max"].fillna(999999999)
    dataframe.loc[:, "Min"] = dataframe.loc[:, "Min"].fillna(0)
    dataframe = dataframe.to_dict("records")
    rides = {}
    for dictionary in dataframe:
        rides[dictionary["Name"]] = Ride(
            dictionary["Name"],
            (dictionary["Min"], dictionary["Max"]),
            dictionary["Description"],
            dictionary["Working"],
        )
    return rides


class Food_Item:
    def __init__(self, name, cost, amount_left) -> None:
        self.name = name
        self.cost = cost
        self.amount_left = amount_left


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
            ) for i in range(len(self.item_names))
        ]

    def display_foods(self, console: Console, discount=0) -> None:
        os.system("cls")
        console.print(f"Welcome to {self.name}\n\n", justify="center")
        console.print(f"Menu", justify="center")
        console.print(f'{"":-^30}', justify='center')
        print_half = self.dataframe.get(['Items', 'Price'])
        console.print(print_half.to_string(index=False), justify="center")

