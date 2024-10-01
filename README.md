# Graphing Constantly Changing Data
### Requirements
* Python 3
* Pandas 2
* Numpy 2
* Matplotlib 3
### Use
this project shows that it is possible to continue having a graph running and updating in matplotlib. the same functions used here could be used for many other things such as keeping track of live data like the stock market.
## Data.py
### Description
Data.py is a script that generates random 5 x 5 pandas DataFrames with values form 0 to 100 filling the DataFrames
## Graph.py
### Description
Graph.py pulls the random DataFrame from Data.py and puts it into a 3D scatter plot. this scatter plaot is then updated every second with more data.
### Usage
To run Graph.py simply put both Graph.py and Data.py into your python 3 environment and run the command
```
python3 Graph.py
```
