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

Example:

``` python
import numpy as np
xpoints = np.array([0, 6])
ypoints = np.array([0, 25])

plt.plot(xpoints, ypoints)
plt.show()
```

### Plotting Without Line

Use `"o"` for markers only:

``` python
plt.plot(xpoints, ypoints, "o")
plt.show()
```

### Multiple Points

``` python
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([1, 4, 0, 6])

plt.plot(xpoints, ypoints)
plt.show()
```

------------------------------------------------------------------------

## Matplotlib Markers

Use `marker=`:

``` python
plt.plot(xpoints, ypoints, marker="o")
plt.plot(xpoints, ypoints, marker="*")
```

### Format Strings (fmt)

Syntax:

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

``` python
plt.subplot(1, 2, 1)
plt.subplot(1, 2, 2)
```

### Title & Supertitle

``` python
plt.suptitle("MY SHOP")
```

------------------------------------------------------------------------

## Matplotlib Scatter

``` python
plt.scatter(x, y)
plt.show()
```

------------------------------------------------------------------------

## Matplotlib Bars

``` python
plt.bar(x, y, color="r")
plt.barh(x, y)
```

------------------------------------------------------------------------

## Matplotlib Histogram

``` python
data = np.random.normal(150, 10, 1000)
plt.hist(data, bins=16, color="lightblue", edgecolor="black")
```

------------------------------------------------------------------------

## Matplotlib Pie Chart

``` python
plt.pie(y, labels=mylabels)
plt.legend(title="Grades")
plt.show()
```
