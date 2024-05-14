"""
NAME: Graph.py
PURPOSE: Simulate graphing constantly changing data
DATE:  5/7/24
PROGRAMMER: Dr Hac
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np
import Data

Data = Data.Data()
fig = plt.figure()
# create 3D subplot
ax = fig.add_subplot(111, projection='3d')


def create(i):
    ax.clear()
    # reroll the data set
    Data.update()
    print('Data1 \n', Data.get())
    for index in Data.get().index:
        for column in Data.get().columns:
            # graph data pulled from the Data.Data() dataframe
            ax.scatter3D(index, column, Data.get().loc[index, column])


# update the graph based on the create() function
a = FuncAnimation(fig, create)
plt.show()

