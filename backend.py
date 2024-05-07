from math import *
import os
import subprocess

subprocess.run(["C:\Program" + " Files\Python310\python.exe","-m",'pip','install','pandas'])
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
    dataframe.iloc[:,2].fillna(inf)
    dataframe.iloc[:,1].fillna(0)
    dataframe = dataframe.to_dict('records')
    rides = {}
    for dictionary in dataframe:
        rides[dictionary["Name"]] = Ride(dictionary['Name'],(dictionary['Min'], dictionary['Max']), dictionary['Description'], dictionary['Working'])
    return rides

class Restaurant:
    def __init__(self, filename) -> None:
        file = pd.read_csv(filename)
        file.to_dict('records')
        