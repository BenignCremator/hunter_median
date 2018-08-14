#!/usr/bin/python3

from hunter_median import hunter_median as h_med

import numpy as np
from matplotlib import pyplot as plt

#  Big O plots



#  Now lets calculate some datasets distributions and see how they fair.
#  We start with a dataset size of 1000.
dsize = 1000

#  Uniform (flat) distribution

dataset = np.random.random (size=dsize)

###  Plot of distribution

#fit = np.mean(dataset)
#plt.plot(dataset, fit, '-o')
plt.hist (dataset, normed=True)
plt.xlabel ("Random Values")
plt.ylabel ("Occurances of Values Within Dataset")
plt.title ('Distribution and Averaging Methods upon '+ chr(dsize) +" Data Points")

#  Plot of various averging methods

###  Hunter Median
(hi_med1, hi_med2, lo_med1, lo_med2) = h_med(dataset)

plt.plot ([hi_med1, hi_med1], [0, 1.2], linestyle='--', color='r', label='Hunter Median Hi')
plt.plot ([lo_med1, lo_med1], [0, 1.2], linestyle='--', color='r', label="Hunter Median Lo")

###  Show Plot
plt.show()

#  Normal distribution

