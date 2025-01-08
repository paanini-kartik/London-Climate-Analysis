import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sklearn

df = pd.read_csv("london_weather.csv")

# Putting columns of csv into arrays

arrDate = range(len(df["date"])) # Days since start
arrCloud = df["cloud_cover"] # Okla index
arrSunshine = df["sunshine"] # Hrs of sunshine
arrRad = df["global_radiation"] # Watts per square meter (intensity)
arrMaxTemp = df["max_temp"] # Degrees Celsius
arrMinTemp = df["min_temp"] # Degrees Celsius
arrMeanTemp = df["mean_temp"] # Degrees Celsius
arrRain = df["precipitation"] # mm
arrPressure = df["pressure"] # Pa

# Turning this into a 2d array

figures = np.array([arrDate, arrCloud, arrSunshine, arrRad, arrMaxTemp, arrMinTemp, arrMeanTemp, arrRain, arrPressure])
figureNames = ["Date", "Cloud Cover", "Sunshine", "Global Radiation", "Max Temp", "Min Temp", "Mean Temp", "Precipitation", "Pressure"]

# Create function to make graph versus time (iterate over multiple different choices of y axes)

def makeGraphDate(x, y, startDate, endDate, colour, density, type):

  xScatter = []
  yScatter = []

  if density == 1:
    if type == 0:
      plt.scatter(x[startDate:endDate], y[startDate:endDate], color = colour)
    else:
      plt.plot(x[startDate:endDate], y[startDate:endDate], color = colour)

  else: # Adjusting density of points
    for i in range(startDate, endDate):
      if i%density == 0:
        xScatter.append(x[i])

    for i in range(startDate, endDate):
      if i%density == 0:
        yScatter.append(y[i])

    if type == 0:
      plt.scatter(xScatter, yScatter, color = colour)
    else:
      plt.plot(xScatter, yScatter, color=colour)

# Create function to make graph with variety of axes

def makeGraph(x, y, colour, density, type):

  xScatter = []
  yScatter = []

  if density == 1:
    if type == 0:
      plt.scatter(x, y, color = colour)
    else:
      plt.plot(x, y, color = colour)

  else: # Adjusting density of points  
    for i in range(len(x)):
      if i%density == 0:
        xScatter.append(x[i])

    for i in range(len(x)):
      if i%density == 0:
        yScatter.append(y[i])

    if type == 0:
      plt.scatter(xScatter, yScatter, color=colour)
    else:
      plt.plot(xScatter, yScatter, color=colour)

# Create various graphs

def trendLine(x, y, colour, indexX, indexY):
  # Create a DataFrame for easier plotting with Seaborn
  data = {figureNames[indexX]: x, figureNames[indexY]: y}
  df_weather = pd.DataFrame(data)
  # Plot with Seaborn
  sns.regplot(x=figureNames[indexX], y=figureNames[indexY], data=df_weather, scatter=False, line_kws={'color': colour, 'linestyle': '--'})
  plt.show()

isContinue = True

while isContinue:  

  graphType = int(input("Would you like to make a graph with one figure and time? (Type 1), compare two figures? (Type 2) or input data to predict? (Type 3): "))

  # Graph comparing time & data

  if graphType == 1:

    print("List of Figures:\n")

    for i in range(len(figures)):
      print(str(i+1) + ". " + figureNames[i])

    indexWanted = int(input("Which figure do you want to compare against time?: "))
    startDate = int(input("What date do you want the graph to start at? (Days after 1979/01/01): "))
    endDate = int(input("What date do you want the graph to end at? (Days after 1979/01/01)"))
    colour = input("What colour would you like the graph to be? (r,g,b, etc.): ")
    lineColour = input("What colour would you like the trend line to be? (r,g,b, etc.): ")
    density = int(input("How dense would you like the graph to be? (1 is no change, 2 is every other point, etc.): "))
    type = int(input("Would you like to make a line graph or a scatter plot? (Type 0 for scatter plot), any other number for line graph: "))

    makeGraphDate(figures[0], figures[indexWanted-1], startDate, endDate, colour, density, type)
    plt.xlabel("Date (Days since 1979/01/01)")
    plt.ylabel(figureNames[indexWanted-1])
    plt.title(figureNames[indexWanted-1] + " vs Date")
    plt.grid()
    trendLine(figures[0][startDate:endDate], figures[indexWanted-1][startDate:endDate], lineColour, 0, indexWanted-1)
    plt.show()

  if graphType == 2:

    print("List of Figures:\n")

    for i in range(len(figures)):
      print(str(i+1) + ". " + figureNames[i])


    indexWanted1 = int(input("Which figure do you want on the x axis?: "))
    indexWanted2 = int(input("Which figure do you want on the y axis?: "))
    colour = input("What colour would you like the graph to be? (r,g,b, etc.): ")
    lineColour = input("What colour would you like the trend line to be? (r,g,b, etc.): ")
    density = int(input("How dense would you like the graph to be? (1 is no change, 2 is every other point, etc.) "))
    type = int(input("Would you like to make a line graph or a scatter plot? (Type 0 for scatter plot), any other number for line graph: "))

    makeGraph(figures[indexWanted1-1], figures[indexWanted2-1], colour, density, type)

    plt.xlabel(figureNames[indexWanted1-1])
    plt.ylabel(figureNames[indexWanted2-1])
    plt.title(figureNames[indexWanted1-1] + " vs " + figureNames[indexWanted2-1])
    plt.grid()
    trendLine(figures[indexWanted1-1], figures[indexWanted2-1], lineColour, indexWanted1-1, indexWanted2-1)

  isContinue = True if input("Would you like to make another graph? (y/n) ") == "y" else False
