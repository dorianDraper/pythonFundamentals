"""
SciPy Significance Tests

In statistics, statistical significance means that the result that was produced
has a reason behind it, it was not produced randomly, or by chance.
SciPy provides us with a module called ' scipy.stats ', which has functions for
performing statistical significance tests.

Check StatisticalConcepts.txt for more detail.

Here are some techniques and keywords that are important when performing such tests:

Hypothesis in Statistics

    Hypothesis is an assumption about a parameter in population.

Null Hypothesis

    It assumes that the observation is not stastically significant.

Alternate Hypothesis

    It assumes that the observations are due to some reason.
    Its alternate to Null Hypothesis. Example:

        For an assessment of a student we would take:

            "student is worse than average" - as a null hypothesis, and:
            "student is better than average" - as an alternate hypothesis.

One tailed test

    When our hypothesis is testing for one side of the value only,
    it is called "one tailed test". Example:

        For the null hypothesis:

            "the mean is equal to k", we can have alternate hypothesis:
            "the mean is less than k", or:
            "the mean is greater than k"

Two tailed test

    When our hypothesis is testing for both side of the values. Example:

        For the null hypothesis:

            "the mean is equal to k", we can have alternate hypothesis:
            "the mean is not equal to k"

        In this case the mean is less than, or greater than k, and both sides are to be checked.

Alpha value

    Alpha value is the level of significance. Example:

        How close to extremes the data must be for null hypothesis to be rejected.

            It is usually taken as 0.01, 0.05, or 0.1.
P value

    P value tells how close to extreme the data actually is.
    P value and alpha values are compared to establish the statistical significance.
    If p value <= alpha we reject the null hypothesis and say that the data
    is statistically significant, Otherwise we accept the null hypothesis.

T-Test

    T-tests are used to determine if there is significant deference between means
    of two variables, and lets us know if they belong to the same distribution.
    It is a two tailed test. The function << ttest_ind() >> takes two samples of
    same size and produces a tuple of t-statistic and p-value.
    Example: Find if the given values v1 and v2 are from same distribution:
"""
from scipy.stats import ttest_ind
import numpy as np

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print (res)
#If you want to return only the p-value, use the pvalue property: Example
res = ttest_ind(v1, v2).pvalue
print (res)
"""
KS-Test

KS test is used to check if given values follow a distribution.
The function takes the value to be tested, and the CDF as two parameters.
A CDF can be either a string or a callable function that returns the probability.
It can be used as a one tailed or two tailed test.
By default it is two tailed. We can pass parameter alternative as a string of
one of two-sided, less, or greater.
Example: Find if the given value follows the normal distribution:
"""
import numpy as np
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')

print (res)
"""
Statistical Description of Data

In order to see a summary of values in an array, we can use the << describe() >> function.
It returns the following description:

    number of observations (nobs)
    minimum and maximum values = minmax
    mean
    variance
    skewness (asymetry)
    kurtosis (measure, curtosis)

Example: Show statistical description of the values in an array:
"""
import numpy as np
from scipy.stats import describe

v = np.random.normal(size=100)

res = describe(v)

print (res)
"""
Normality Tests (Skewness and Kurtosis)

Normality tests are based on the skewness and kurtosis.
The << normaltest() >> function returns p value for the null hypothesis:
"x comes from a normal distribution".

 Skewness:

    A measure of symmetry in data.
    For normal distributions it is 0.
    If it is negative, it means the data is skewed left.
    If it is positive it means the data is skewed right.

Kurtosis:

A measure of whether the data is heavy or lightly tailed to a normal distribution.
Positive kurtosis means heavy tailed.
Negative kurtosis means lightly tailed.

Example: Find skewness and kurtosis of values in an array:
"""
import numpy as np
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

print (skew(v))
print (kurtosis(v))
#Example: Find if the data comes from a normal distribution:
import numpy as np
from scipy.stats import normaltest

v = np.random.normal(size=100)

print (normaltest(v))
