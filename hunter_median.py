#!/usr/bin/python3

def hunter_median(data_set):
    '''Accepts a numerical 1D data_set in list, tuple, or numpy array form.
    The data set is assumed to be unordered and of uneven distribution.
    Iterates over the data set three times to find values that approximate
    the mean, the median, etc.
    '''

    
    maxi, mini = data_set[0], data_set[0] #  Maximum and Minimum values within data set
    total_num = len(data_set)  #  Total number of elements in data_set
    
    for x in data_set:
        if x > maxi: maxi = x
        if x < mini: mini = x

    mid_point = (high_num + low_num) / 2.0

    high_total, low_total = 0, 0
    high_num, low_num = 0, 0
    for x in data_set:
        if x > mid_point:
            high_total, high_num = high_total + x, high_num + 1
        if x < mid_point:
            low_total, low_num = low_total + x, low_num + 1

    high_ave, low_ave, ave = high_total / high_num, low_total / low_num, \
                             (high_total+low_total)/(total_num)

    high_med1 = (maxi - mini) / (high_num / total_num)
    high_med2 = (high_ave - low_ave) / (high_num / total_num)

    low_med1 = (maxi - mini) / (low_num / total_num)
    low_med2 = (high_ave - low_ave) / (low_num / total_num)

    return (high_med1, high_med2, low_med1, low_med2)
