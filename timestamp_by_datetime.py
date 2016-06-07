# ADW, 07 June 2016
# Run this inside the directory with the images

import glob
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt

files = sorted(glob.glob('*.jpg'))
f0 = files[0]

timestamps = []
unixtimes = []

# For the "strptime" function for working with time stamps,
# see http://www.tutorialspoint.com/python/time_strptime.htm
start_time = dt.datetime.strptime(files[0], "Img%Y-%m-%d %H.%M.%S.jpg")
seconds_since_start = []

for fi in files:
  timestamp = dt.datetime.strptime(fi, "Img%Y-%m-%d %H.%M.%S.jpg")
  timestamps.append(timestamp)
  # Writing this as an integer instead of timedelta with total_seconds
  seconds_since_start.append( (timestamp - start_time).total_seconds() )
seconds_since_start = np.array(seconds_since_start)


# Plot the results

plt.plot(seconds_since_start, 'k.');
plt.xlabel('Image number (sequential from start)', fontsize=16)
plt.ylabel('Real time since start of experiment [seconds]', fontsize=16)

plt.show()


# ... after this, it will be a matter of looking for legitimate breaks in time
# that are related to pauses in the experiment (e.g., laser scans)
# and replacing them with a number of seconds elapsed that comes
# immediately after those time-stamps that precede the laser scans.

# Also, using this method of working through the time stamps allows you to
# delete pictures before you sort them -- because it just reads the 
# time stamps. Just so long as you don't create a big break in time without
# remembering that it was you who made it!

