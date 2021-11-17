"""
Matplotlib Subplots

Display Multiple Plots

With the < subplots() > function you can draw multiple plots in one figure:
Example: Draw 2 plots:
"""
import matplotlib.pyplot as plt 
import numpy as np 

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
"""
The subplots() Function

The < subplots() > function takes three arguments that describes the layout of the figure.
The layout is organized in rows and columns, which are represented by the first and second argument.
The third argument represents the index of the current plot.

plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

 
plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.

So, if we want a figure with 2 rows an 1 column (meaning that the two plots 
will be displayed on top of each other instead of side-by-side), we can write the syntax like this:
Example: Draw 2 plots on top of each other:
"""
import matplotlib.pyplot as plt
import numpy as np 

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()
"""
You can draw as many plots you like on one figure, just descibe the 
number of rows, columns, and the index of the plot.
Example: Draw 6 plots:
"""
import matplotlib.pyplot as plt 
import numpy as np 

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x1,y1)

x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x2,y2)

x3 = np.array([0, 1, 2, 3])
y3 = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x3,y3)

x4 = np.array([0, 1, 2, 3])
y4 = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x4,y4)

x5 = np.array([0, 1, 2, 3])
y5 = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x5,y5)

x6 = np.array([0, 1, 2, 3])
y6 = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x6,y6)

plt.show()
"""
Title

You can add a title to each plot with the < title() > function:
Example: 2 plots, with titles:
"""
import matplotlib.pyplot as plt 
import numpy as np 

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

plt.show()
"""
Super Title

You can add a title to the entire figure with the < suptitle() > function:
Example: Add a title for the entire figure:
"""
import matplotlib.pyplot as plt 
import numpy as np 

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

plt.suptitle("MY SHOP")
plt.show()