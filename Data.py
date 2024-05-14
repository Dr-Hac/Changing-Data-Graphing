"""
NAME: Data.py
PURPOSE: Simulate a constantly changing dataset
DATE:  5/7/24
PROGRAMMER: Dr Hac
"""

import numpy as np
import pandas as pd


class Data:
    def __init__(self):
        # create a random 5 by 5 dataframe
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(5, 5)))

    def update(self):
        # create a random 5 by 5 dataframe
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(5, 5)))

    def get(self):
        # return the randomized 5 by 5 dataframe
        return self.df
