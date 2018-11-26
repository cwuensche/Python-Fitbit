import os, time, glob, json
import numpy as np
import matplotlib.pyplot as plt
import datetime

files = sorted( glob.glob("data/*"), key=os.path.getmtime )
highest_bpm = 0

daily_bpm = []
daily_day = []
plt.xlabel( 'Day' )
plt.ylabel( 'Heart rate' )
plt.title( 'Daily Max heartrate for September 2016')

for filename in files:
	if "heart_rate-2016-09" in filename:
		max_bpm = 0
		heartrate_date = ""
		with open( filename, 'r' ) as f:
			heartrate_dictionary = json.load( f )

			for heartrate in heartrate_dictionary:
				if ( int( heartrate['value']['bpm'] ) > max_bpm ):
					max_bpm = heartrate['value']['bpm']
					if ( "" == heartrate_date ):
						heartrate_date = heartrate['dateTime'].partition(' ')
						daily_day.append( heartrate_date[0] )
			daily_bpm.append( max_bpm )
		if ( 0 == highest_bpm or max_bpm > highest_bpm ):
			highest_bpm = max_bpm

plt.plot( np.array( daily_bpm ) )
plt.show()
