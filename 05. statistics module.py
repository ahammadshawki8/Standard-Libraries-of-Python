# statistics module

# statistics module is very important module for working with statistics in python
# it provides us with various important statistical functions and tools which are really helpful.

# first we need to import the module.
import statistics as stat

# lets see all the methods and attributes of statistics module
print(dir(stat))

# we can see here:-
# ['Counter', 'Decimal', 'Fraction', 'NormalDist', 'StatisticsError', '__all__', '__builtins__', 
# '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_coerce',
# '_convert', '_exact_ratio', '_fail_neg', '_find_lteq', '_find_rteq', '_isfinite', '_normal_dist_inv_cdf',
# '_ss', '_sum', 'bisect_left', 'bisect_right', 'erf', 'exp', 'fabs', 'fmean', 'fsum', 'geometric_mean',
# 'groupby', 'harmonic_mean', 'hypot', 'itemgetter', 'log', 'math', 'mean', 'median', 'median_grouped',
# 'median_high', 'median_low', 'mode', 'multimode', 'numbers', 'pstdev', 'pvariance', 'quantiles', 'random',
# 'sqrt', 'stdev', 'tau', 'variance']


# lets discover some of the methods and attributes.
a=[20, 20, 20, 23, 34, 40, 45, 56, 67, 67, 67, 77]


# we can see we have exp, sqrt, log here. we also have the value of tau.
print(stat.exp(45)) 
    # it raises e to the power of the input
print(stat.sqrt(90))
print(stat.log(100))
print(stat.tau)


# here we have different types of mean such as mean, harmonic_mean, geometric_men, fmean.
print(stat.mean(a))
print(stat.harmonic_mean(a))
    # The harmonic mean, sometimes called the subcontrary mean, is the
    # reciprocal of the arithmetic mean of the reciprocals of the data,
    # and is often appropriate when averaging quantities which are rates
    # or ratios, for example speeds. Example:
    # Suppose an investor purchases an equal value of shares in each of
    # three companies, with P/E (price/earning) ratios of 2.5, 3 and 10.
    # What is the average P/E ratio for the investor's portfolio?
    # >>> harmonic_mean([2.5, 3, 10])  # For an equal investment portfolio.
    # 3.6
    # Using the arithmetic mean would give an average of about 5.167, which is too high.

print(stat.geometric_mean(a))
    # converts data to floats abd compute the geometric mean.

print(stat.fmean(a))
    # it is same as mean(), but it runs faster than mean and always returns a float.


# we also have different types of medians such as median, median_group, median_high, median_low.
print(stat.median(a))
print(stat.median_grouped(a))
    # Return the 50th percentile (median) of grouped continuous data.
print(stat.median_high(a))
    # Return the high median of data.
print(stat.median_low(a))
    # Return the low median of data.


# we also have different kinds of mode such as mode and multimode
print(stat.mode(a))
print(stat.multimode(a)) 
    # returns all the modes if there are multiple modes


# we have 2 types of variance such as variance and pvariance.
print(stat.variance(a))
    # Return the sample variance of data.

    # data should be an iterable of Real-valued numbers, with at least two
    # values. The optional argument xbar, if given, should be the mean of
    # the data. If it is missing or None, the mean is automatically calculated.

    # Use this function when your data is a sample from a population. To
    # calculate the variance from the entire population, see ``pvariance``.

print(stat.pvariance(a))
    # pvariance stands for population variance
    # return the population variance of ``data``.

    # data should be a sequence or iterable of Real-valued numbers, with at least one
    # value. The optional argument mu, if given, should be the mean of
    # the data. If it is missing or None, the mean is automatically calculated.

    # Use this function to calculate the variance from the entire population.
    # To estimate the variance from a sample, the ``variance`` function is
    # usually a better choice.


# we have 2 types of stdev (standerd deviation) here stdev and pstdev.
print(stat.stdev(a))
    # stdev just returns the square root of the sample variance
print(stat.pstdev(a))
    # pstdev returns the square root of the population variance


# we also have fabs, fsum, hypot, groupby
print(stat.fabs(-576.44)) 
    # return the absolute value of input. faster than abs.
print(stat.fsum(a)) 
    # simmilar to sum() but faster
print(stat.hypot(3,4,6,5,7)) 
    # gives the distance between origin and the input point in n-th dimention.


# quantiles() function is used for dividing data into n continuous intervals with equal probablity.
# it returns a lit of (n-1) cut points separating the intervals. n is set to 4 by default.
print(stat.quantiles(a,n=5))

# we also have groupby() method. which is same as the groupby method of itertool module.
# it groups the element of the iterable according to a key function
a=[("a",1),("a",2),("b",1),("b",2)]
b=stat.groupby(a,lambda x: x[0])  # this lambda function called key function
for key,group in b:
    print(key+" : ",list(group))

