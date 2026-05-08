# Matplotlib Notes

## Matplotlib

Matplotlib is a Python library for data visualization. It allows you to
create a wide range of plots and charts, such as line plots, scatter
plots, bar charts, histograms, and more.

## Pyplot

Most of the Matplotlib utilities lie under the pyplot submodule, and are
usually imported under the `plt` alias.

### Plotting x and y points

The `plot()` function is used to draw points (markers) in a diagram.\
By default, it draws a line from point to point.

The function takes parameters for specifying points in the diagram.
Parameter 1 is an array containing the points on the x-axis.
Parameter 2 is an array containing the points on the y-axis.
If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.

Example:

``` python
import numpy as np
xpoints = np.array([0, 6])
ypoints = np.array([0, 25])

plt.plot(xpoints, ypoints)
plt.show()
```

### Plotting Without Line

To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

``` python
plt.plot(xpoints, ypoints, "o")
plt.show()
```

### Multiple Points

You can plot as many points as you like, just make sure you have the same number of points in both axis.

``` python
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([1, 4, 0, 6])

plt.plot(xpoints, ypoints)
plt.show()
```

------------------------------------------------------------------------

## Matplotlib Markers


You can use the keyword argument `marker` to emphasize each point with a specified marker:

``` python
# Eg. Mark each point with a circle

plt.plot(xpoints, ypoints, marker="o")
plt.show()

# Eg. mark each point with a star (*)

plt.plot(xpoints, ypoints, marker="*")
plt.show()
```

### Format Strings (fmt)

You can also use the shortcut string notation parameter to specify the marker.
This parameter is also called fmt, and is written with this syntax:

    marker | line | color

### Line Reference

-   `:` dotted\
-   `-` solid\
-   `--` dashed\
-   `-.` dash-dot

### Color Reference

-   `r` red\
-   `g` green\
-   `b` blue\
-   `c` cyan

Example:

``` python
plt.plot(xpoints, ypoints, "o:r")
```

### Marker Size

You can use the keyword argument `markersize` or the shorter version, ms to set the size of the markers:

``` python
plt.plot(xpoints, ypoints, marker="o", ms=20)
```

### Marker Edge & Face Color

``` python
plt.plot(xpoints, ypoints, marker="o", ms=10, mec="r", mfc="yellow")
```

------------------------------------------------------------------------

## Matplotlib Line

### Linestyle

``` python
plt.plot(xpoints, ypoints, linestyle="dotted")
plt.plot(xpoints, ypoints, linestyle="dashed")
```

Short syntax: - `ls` - `:` dotted\
- `--` dashed

### Line Color

``` python
plt.plot(xpoints, ypoints, color="r")
```

### Line Width

``` python
plt.plot(xpoints, ypoints, lw=10)
```

### Multiple Lines

``` python
y1 = np.array([2, 3, 5, 6])
y2 = np.array([3, 5, 8, 2])
plt.plot(y1)
plt.plot(y2)
```

------------------------------------------------------------------------

## Matplotlib Labels and Title

``` python
plt.xlabel("Average student")
plt.ylabel("Average height")
plt.title("My Plot")
```

### Font Properties

``` python
font1 = {'family':'serif','color':'blue','size':15}
font2 = {'family':'serif','color':'blue','size':20}

plt.xlabel("Average student", fontdict=font1)
plt.ylabel("Average Height", fontdict=font1)
plt.title("Title", fontdict=font2)
```

### Title Position

``` python
plt.title("Title", loc="left")
```

------------------------------------------------------------------------

## Matplotlib Subplots

### Display Multiple Plots

With the `subplot()` function you can draw multiple plots in one figure:

### The `subplot()` Function

The subplot() function takes three arguments that describes the layout of the figure.

The layout is organized in rows and columns, which are represented by the first and second argument.

The third argument represents the index of the current plot.


``` python
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
```

### Title & Supertitle

``` python
plt.suptitle("MY SHOP")
```

------------------------------------------------------------------------

## Matplotlib Scatter

### Creating Scatter Plots
With Pyplot, you can use the `scatter()` function to draw a scatter plot.

The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for the values on the y-axis:


``` python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([4, 6, 7, 4, 7, 11, 12, 13, 12, 15, 19, 15, 3, 14, 17])
y = np.array([99, 93, 97, 99, 105, 110,113, 112, 110, 107, 111, 92, 113, 115, 117])

plt.scatter(x, y)
plt.show()
```

------------------------------------------------------------------------

## Matplotlib Bars
### Creating Bars
With Pyplot, you can use the bar() function to draw bar graphs:

### Horizontal Bars
If you want the bars to be displayed horizontally instead of vertically, use the barh() function:

### Bar Width
The bar() takes the keyword argument width to set the width of the bars:

### Bar Height
The barh() takes the keyword argument height to set the height of the bars:



``` python
x = np.array(["Munich", "Kathmandu", "NewYork", "London"])
y = np.array([10, 25, 21, 12])

plt.xlabel("Cities around the globe")
plt.ylabel("Average temperature of a year(Celsus)")
plt.title("Comarision of the average tem between cities")

plt.bar(x, y, color = "r")

plt.show()
```

------------------------------------------------------------------------

## Matplotlib Histogram

### Histogram

A histogram is a graph showing frequency distributions.

In Matplotlib, we use the hist() function to create histograms.

The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.


``` python
data = np.random.normal(150, 10, 1000)
plt.hist(data, bins=16, color="lightblue", edgecolor="black")
plt.show()
```

------------------------------------------------------------------------

## Matplotlib Pie Chart

``` python
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

```
