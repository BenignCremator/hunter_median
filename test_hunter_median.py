#!/usr/bin/python3

import hunter_median, d_roll

import numpy as np
from matplotlib import pyplot as plt

#  Big O plots



#  Now lets calculate some datasets distributions and see how they fair.
#  We start with a dataset size of 1000.
dsize = 1000

#  Uniform (flat) distribution

dataset = np.random.random(size=dsize)

###  Plot of distribution

plt.plot(h, dataset, '-o')
plt.hist(h, normed=True)
plt.show()

#  Plot of various averging methods

###  Hunter Median
(hi_med1, hi_med2, lo_med1, lo_med2) = hunter_median(dataset)


#  Normal distribution

