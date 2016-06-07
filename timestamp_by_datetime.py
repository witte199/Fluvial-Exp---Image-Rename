# ADW, 07 June 2016

import glob
import datetime as dt
import numpy as np
import os 
from matplotlib import pyplot as plt

# Run this inside the directory with the images
cwd = r'E:\151124_MC_DW_IW_01\151124_MC_DW_IW_01_Photos'
os.chdir(cwd)

files = sorted(glob.glob('*.jpg'))
f0 = files[0]

timestamps = []

# For the "strptime" function for working with time stamps,
# see http://www.tutorialspoint.com/python/time_strptime.htm
experiment_start = dt.datetime.strptime(files[0], "Img%Y-%m-%d %H.%M.%S.jpg")
seconds_since_start = []

for fi in files:
  timestamp = dt.datetime.strptime(fi, "Img%Y-%m-%d %H.%M.%S.jpg")
  timestamps.append(timestamp)
  # Writing this as an integer instead of timedelta with total_seconds
  seconds_since_start.append( (timestamp - experiment_start).total_seconds() )
seconds_since_start = np.array(seconds_since_start)

timestampsara = np.array(timestamps)
scan_start_times = np.array([    dt.datetime(2016, 11, 24, 08, 59, 37),
                                 dt.datetime(2016, 11, 24, 09, 28, 03),
                                 dt.datetime(2016, 11, 24, 10, 08, 25),
                                 dt.datetime(2016, 11, 24, 10, 48, 16),
                                 dt.datetime(2016, 11, 24, 11, 24, 51),
                                 dt.datetime(2016, 11, 24, 12, 03, 24),
                                 dt.datetime(2016, 11, 24, 12, 40, 42),
                                 dt.datetime(2016, 11, 24, 13, 55, 34),
                                 dt.datetime(2016, 11, 24, 14, 38, 00),
                                 dt.datetime(2016, 11, 24, 15, 19, 05),
                                 dt.datetime(2016, 11, 24, 15, 57, 17),
                                 dt.datetime(2016, 11, 24, 16, 31, 01),
                                 dt.datetime(2016, 11, 24, 17, 08, 44),
                                 dt.datetime(2016, 11, 24, 17, 44, 55),
                                 dt.datetime(2016, 11, 24, 18, 22, 01),
                                 dt.datetime(2016, 11, 25, 10, 11, 19),
                                 dt.datetime(2016, 11, 25, 10, 47, 41),
                                 dt.datetime(2016, 11, 25, 11, 29, 06),
                                 dt.datetime(2016, 11, 25, 12, 05, 24),
                                 dt.datetime(2016, 11, 25, 13, 27, 51),
                                 dt.datetime(2016, 11, 25, 14, 04, 23),
                                 dt.datetime(2016, 11, 25, 14, 41, 58),
                                 dt.datetime(2016, 11, 25, 15, 18, 42),
                                 dt.datetime(2016, 11, 25, 15, 55, 59)])

scan_end_times = np.array([      dt.datetime(2016, 11, 24, 09, 06, 23),
                                 dt.datetime(2016, 11, 24, 09, 38, 25),
                                 dt.datetime(2016, 11, 24, 10, 18, 16),
                                 dt.datetime(2016, 11, 24, 11, 00, 11),
                                 dt.datetime(2016, 11, 24, 11, 33, 23),
                                 dt.datetime(2016, 11, 24, 12, 10, 43),
                                 dt.datetime(2016, 11, 24, 13, 25, 52),
                                 dt.datetime(2016, 11, 24, 14, 01, 51),
                                 dt.datetime(2016, 11, 24, 14, 47, 47),
                                 dt.datetime(2016, 11, 24, 15, 25, 17),
                                 dt.datetime(2016, 11, 24, 16, 03, 21),
                                 dt.datetime(2016, 11, 24, 16, 38, 43),
                                 dt.datetime(2016, 11, 24, 17, 14, 55),
                                 dt.datetime(2016, 11, 24, 17, 51, 59),
                                 dt.datetime(2016, 11, 25, 09, 41, 40),
                                 dt.datetime(2016, 11, 25, 10, 17, 40),
                                 dt.datetime(2016, 11, 25, 10, 58, 11),
                                 dt.datetime(2016, 11, 25, 11, 35, 23),
                                 dt.datetime(2016, 11, 25, 12, 57, 50),
                                 dt.datetime(2016, 11, 25, 13, 43, 23),
                                 dt.datetime(2016, 11, 25, 14, 11, 57),
                                 dt.datetime(2016, 11, 25, 14, 48, 41),
                                 dt.datetime(2016, 11, 25, 15, 25, 58),
                                 dt.datetime(2016, 11, 25, 00, 00, 00)])
                                 
scan_start_times - scan_end_times

for start_time in start_times[::-1]:
    after_start = timestampsara > start_time
    seconds_since_start[after_start] -= 
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



