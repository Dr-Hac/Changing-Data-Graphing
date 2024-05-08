"""
NAME: Graph.py
PURPOSE: Simulate graphing constantly changing data
DATE:  5/7/24
PROGRAMMER: Dr Hac
"""

import matplotlib.pyplot as plt
import numpy
from matplotlib.animation import FuncAnimation
import Data
import pandas as pd
import numpy as np

Data1 = Data.Data()
Data2 = Data.Data()
Data3 = Data.Data()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def create(i):
    ax.clear()
    Data1.update()
    Data2.update()
    Data3.update()
    print('Data1 \n', Data1.get())
    print('Data2 \n', Data2.get())
    print('Data3 \n', Data3.get())
    x = np.array(Data1.get())
    y = x.copy().T
    z = np.array(Data3.get())
    """
    for index in Data.get().index:
        for column in Data.get().columns:
            ax.scatter3D(index, column, Data.get().loc[index, column])
    """
    ax.plot_surface(x, y, z, color='Red', shade=True)


a = FuncAnimation(fig, create)
plt.show()

