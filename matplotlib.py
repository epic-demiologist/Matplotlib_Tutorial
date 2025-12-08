import matplotlib
print(matplotlib.__version__)

## Pyplot: Pyplot is the submodule under matplotlib

import matplotlib.pyplot as plt

## Basic Plotting

# Drawing a line from one position to another postion
import numpy as np
xpoints = np.array([0, 6])
ypoints = np.array([0, 25])

plt.plot(xpoints, ypoints)
plt.show()

# Plotting without a line

plt.plot(xpoints, ypoints, "o") #shortcut string notation parameter 'o', which means 'rings'.
plt.show()

# Multiple Points

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([1, 4, 0, 6])

plt.plot(xpoints, ypoints)
plt.show()


## PYthon Markers

# Eg. Mark each point with a circle

plt.plot(xpoints, ypoints, marker = "o")
plt.show()

# Eg. mark each point with a star (*)

plt.plot(xpoints, ypoints, marker = "*")
plt.show()


## Format Strings fmt: Parameter is called fmt, and is written
#with this syntax: marker|line|color


plt.plot(xpoints, ypoints, "o:r") # o is marker, : is dotted line(line ref) and r is color red
plt.show()


## Marker size

# Set size of the marker to 20:

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([1, 4, 0, 6])

plt.plot(xpoints, ypoints, marker = "o", ms = 20)
plt.show()

plt.plot(xpoints, ypoints, "o-b", ms = 10) # using string format method
plt.show()



## Marker Edge Color

plt.plot(xpoints, ypoints, marker = "o", ms = 10, mec = "r") # mec = markeredgecolor
plt.show()


## Linestyle

plt.plot(xpoints, ypoints, linestyle = "dotted") #dotted line
plt.show()


plt.plot(xpoints, ypoints, ls = "dashed") # linestyle = ls
plt.show()

plt.plot(xpoints, ypoints, ls = ":") # dotted = :, dashed = --
plt.show()


## Line color

plt.plot(xpoints, ypoints, color = "r")
plt.show()


## Line width


plt.plot(xpoints, ypoints, linewidth = "15")
plt.show()

plt.plot(xpoints, ypoints, lw = "10") # linewidth = lw
plt.show()


## Multiple Lines

y1 = np.array([2, 3, 5, 6])
y2 = np.array([3, 5, 8, 2])

plt.plot(y1) #There are no xpoints. So by defult all x will be 0
plt.plot(y2) #There are no xpoints. So by defult all x will be 0

plt.show()



x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()



## Matplotlib Labels and Title

x = np.array([70, 75, 80, 85, 90, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Avreage student")
plt.ylabel("Average Height")

plt.show()

## Create Title for a plot

x = np.array([70, 75, 80, 85, 90, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Title for this plot")
plt.xlabel("Avreage student")
plt.ylabel("Average Height")

plt.show()


## Set Font Properties for Title and Labels


x = np.array([70, 75, 80, 85, 90, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family': 'serif', 'color': 'blue', 'size': 15}
font2 = {'family': 'serif', 'color': 'blue', 'size': 20}

plt.xlabel("Average student", fontdict = font1)
plt.ylabel("Average Height", fontdict = font1)
plt.title("Title for this plot", fontdict = font2)

plt.plot(x, y)
plt.show()


## Position of the Title

x = np.array([70, 75, 80, 85, 90, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Title for this plot", loc = "left") #Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
plt.xlabel("Avreage student")
plt.ylabel("Average Height")

plt.show()

## Grid 

x = np.array([70, 75, 80, 85, 90, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Title for this plot", loc = "left") #Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
plt.xlabel("Avreage student")
plt.ylabel("Average Height")

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()


## Matplotlib Subplot
#With the subplot() function you can draw multiple plots in one figure:



# Draw two plots

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) #(figure has 1 row, 2 column, and this plot is the first plot)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2) #(figure has 1 row, 2 columns, and this plot is the 2nd one)
plt.plot(x,y)

plt.show()



## plt.subplot(2, 1, 1) = (2 rows, 1 coumn, and plot is the 1st one)


# Draw 6 plots

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1) # 1st plot
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2) # 2nd plot
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3) # 3rd plot
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()



## Titles

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES") # Title for the 1st plot

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME") # Title for 2nd plot

plt.show()




## Super title: You can add a title to the entire figure with 
# the suptitle() function:


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP") # Super title for the whole plot
plt.show()


## Matplotlib Scatter plots

import matplotlib.pyplot as plt
import numpy as np

x = np.array([4, 6, 7, 4, 7, 11, 12, 13, 12, 15, 19, 15, 3, 14, 17])
y = np.array([99, 93, 97, 99, 105, 110,113, 112, 110, 107, 111, 92, 113, 115, 117])


plt.scatter(x, y)
plt.show()



## Matplotlib Barplot

x = np.array(["Munich", "Kathmandu", "NewYork", "London"])
y = np.array([10, 25, 21, 12])

plt.xlabel("Cities around the globe")
plt.ylabel("Average temperature of a year(Celsus)")
plt.title("Comarision of the average tem between cities")

plt.bar(x, y, color = "r", width = 0.1)

plt.show()


# FOr horizonal bars

plt.barh(x, y)
plt.show()



## Matplotlib Histograms


data = np.random.normal(150, 10, 1000) # Genereates an array with 1000 values, with mean = 150 and sd = 10
print(data)

plt.hist(data, bins = 16, color = "lightblue", edgecolor = "Black") #hist() function
plt.show()


## Matplotlib Pie Charts

y = np.array([35, 25, 25, 15])
mylabels = ["Grade 1", "Grade 2", "Grade 3", "Grade 4"]

plt.pie(y, labels = mylabels)
plt.title("Number of students in different grades")

plt.show() 


# Legend with header

y = np.array([35, 25, 25, 15])
mylabels = ["Grade 1", "Grade 2", "Grade 3", "Grade 4"]

plt.pie(y, labels = mylabels)
plt.title("Number of students in different grades")
plt.legend(title = "Grades")

plt.show()















