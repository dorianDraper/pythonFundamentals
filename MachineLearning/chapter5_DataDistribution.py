"""
Data Distribution (Machine Learning)

Earlier in this tutorial we have worked with very small amounts of data
in our examples, just to understand the different concepts.

In the real world, the data sets are much bigger, but it can be difficult
to gather real world data, at least at an early stage of a project.

How Can we Get Big Data Sets?

To create big data sets for testing, we use the Python module NumPy,
which comes with a number of methods to create random data sets, of any size.
Example: Create an array containing 250 random floats between 0 and 5:
"""
import numpy as np

x = np.random.uniform(0.0, 5.0, 250)

print (x)
"""
Histogram

To visualize the data set we can draw a histogram with the data we collected.
We will use the Python module ' Matplotlib ' to draw a histogram.
Learn about the Matplotlib module in our Matplotlib Tutorial.
Example: Draw a histogram:
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)  #histogram with 5 bars
plt.show()
"""
Histogram Explained

We use the array from the example above to draw a histogram with 5 bars.
The first bar represents how many values in the array are between 0 and 1.
The second bar represents how many values are between 1 and 2.
Etc.
Which gives us this result:

    52 values are between 0 and 1
    48 values are between 1 and 2
    49 values are between 2 and 3
    51 values are between 3 and 4
    50 values are between 4 and 5

Note: The array values are random numbers and will not show the exact same result on your computer.
"""
"""
Big Data Distributions

An array containing 250 values is not considered very big, but now you know how to create
a random set of values, and by changing the parameters, you can create the data set as big as you want.
Example: Create an array with 100000 random numbers, and display them using a histogram with 100 bars:
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 10000)

plt.hist(x, 100)    #with 100 bars
plt.show()
"""
Normal Data Distribution

In the previous chapter we learned how to create a completely random array,
of a given size, and between two given values.
In this chapter we will learn how to create an array where the values are concentrated around a given value.
In probability theory this kind of data distribution is known as the normal data distribution,
or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up
with the formula of this data distribution.
Example: A typical normal data distribution:
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5.0, 1.0, 10000)

plt.hist(x, 100)
plt.show()
"""
Note: A normal distribution graph is also known as the bell curve
because of its characteristic shape of a bell.
"""
"""
Histogram Explained

We use the array from the ' numpy.random.normal() ' method, with 100000 values,
to draw a histogram with 100 bars.
We specify that the mean value is 5.0, and the standard deviation is 1.0.
Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.
"""
