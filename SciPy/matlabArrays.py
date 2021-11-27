"""
SciPy Matlab Arrays

We know that NumPy provides us with methods to persist the data in readable formats
for Python. But SciPy provides us with interoperability with Matlab as well.
SciPy provides us with the module ' scipy.io ', which has functions for working with Matlab arrays.

Exporting Data in Matlab Format

The << savemat() >> function allows us to export data in Matlab format.
The method takes the following parameters:

    filename - the file name for saving data.
    mdict - a dictionary containing the data.
    do_compression - a boolean value that specifies wheter to compress the reult or not. Default False.

Example: Export the following array as variable name "vec" to a mat file:
"""
from scipy import io
import numpy as np

arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})
"""
Note: The example above saves a file name "arr.mat" on your computer.
To open the file, check out the "Import Data from Matlab Format" example below:
"""
"""
Import Data from Matlab Format

The << loadmat() >> function allows us to import data from a Matlab file.
The function takes one required parameter:

filename - the file name of the saved data.

It will return a structured array whose keys are the variable names,
and the corresponding values are the variable values.
Example: Import the array from following mat file.:
"""
from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

#Export:
io.savemat('arr.mat', {"vec": arr})

#Import:
mydata = io.loadmat('arr.mat')

print (mydata)
print (mydata['vec'])

print()
#Use the variable name "vec" to display only the array from the matlab data:
"""
Note: We can see that the array originally was 1D, but on extraction it has increased one dimension.
In order to resolve this we can pass an additional argument squeeze_me=True:
"""
from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

#Import:
mydata = io.loadmat('arr.mat', squeeze_me=True)

print (mydata['vec'])
