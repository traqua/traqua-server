##Import Packages + Modules
import numpy as np
import matplotlib.pyplot as plt

##Time and Flow Arrays
flowrate = []
time = []

##Read CSV File (First line is Flow Rate, Second line is Time)
flowrate = np.loadtxt('data.csv',delimiter=',', usecols=(0))
time = np.loadtxt('data.csv',delimiter=',', usecols=(1))
print(flowrate)
print(time)

##Initialisation and plotting of graph/data
plt.interactive(False)
plt.figure()

##Plot point
plt.plot([time], [flowrate], marker='o', markersize=5, color="red")
plt.plot(time, flowrate,color = "blue")

##Label graph
plt.xlabel("Time (Hrs)")
plt.ylabel("Flow Rate (Litres per Second)")
plt.show(block=True)