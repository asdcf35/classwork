from math import *
import os
import sys
if os.name() == "nt":
    os.system(" & 'c:\Program Files\Python310\python.exe' -m pip install pandas")

import pandas as pd
# rides
class Ride:
    def __init__(self, age_range, desc, working) -> None:
        self.min_age, self.max_age = age_range
        self.desc = desc
        self.working = working

    def check_age(self, age) -> bool:
        return self.min_age < age < self.max_age

    def working(self) -> None:
        self.working = not self.working


def rides_from_file(filename="./init_files/rides.csv") -> dict[str, Ride]:
    """
    Making Ride objects from a file

    Parameters
    ---
    filename : str, path object or file-like object
        the filename or object that you wish to use(must work with read_csv)
    """
    dataframe = pd.read_csv(filename)
    dataframe['Max Age'].fillna(inf)
    dataframe['Min Age'].fillna(0)
    dataframe = dataframe.to_dict('records')
    rides = {}
    for dictionary in dataframe:
        rides[dictionary["Name"]] = Ride(
            (dictionary['Min Age'], dictionary['Max Age']), dictionary['Description'], dictionary['Working'])
    return rides

class Restaurant:
    def __init__(self, filename) -> None:
        file = pd.read_csv(filename)
        file.to_dict('records')