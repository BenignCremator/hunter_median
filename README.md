Hunter Median Algorithm test platform

This is a setup to test and compare various averaging, median, and mode finding algorthims.
It is largely uninteresting to anyone except its developer.

The general setup is that several random datasets are created, with differring distribution,
sizes, etc, and the code then uses various averaging type algorthims on them, recording
time spent calculating, memory usage, etc.  Uses PyPlot to create plots comparing the various
metrics.

The intersting tidbit on this, and the reason for creating this, is in the hunter_median
library, which contains a median calculating algorthims that I wrote and am testing, as
a means to learn more about this area of statistics.
