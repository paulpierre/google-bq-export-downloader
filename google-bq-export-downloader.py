intro = """
-----------------------------------
Google Storage BQ Export Downloader
-----------------------------------
by @paulpierre 03-07-2019
Downloads serialized gzip files exported from BigQuery

note: made as-is, didn't bother refactoring once functioning.

URL structure example:
https://storage.googleapis.com/<folder>/<prefix>_export/<prefix>_<year>_<month>_<serialization>.csv.gz

"""

import requests
import sys
import os.path

#pretty colors
class colors:
    green = '\033[1;32;40m'
    red = '\033[1;31;40m'
    reset = '\033[0m'
    grey = '\033[1;30;40m'
    white = '\033[1;39;40m'

#serialization digits character length
char_len = 12

#----------------
# Setup variables
#----------------
folder = 'your-folder'
prefix = 'your-prefix'
start_month = 1
start_year = 2016
serial_error = False

print colors.white + intro + colors.reset


#--------------
#loop structure
#--------------
	#increment year
		#increment month
			#increment serial
				#if error, exit loop

path = 'https://storage.googleapis.com/' + folder +'/' + prefix +'_export/'
_year = start_year
_month = start_month
i = 0

#----------
# Year loop
#----------
while not _year > 2019:
	
	#----------
	# Month loop
	#----------
	while _month < 13:

		#pad single digit months with 0

		if len(str(_month)) is 1:
			month = '0' + str(_month)
		else:
			month = str(_month)

		#i realize there is a datetime function for this
		#but plzSTFU :)


		#-------------------
		# Serialization loop
		#-------------------
		while not serial_error:
	
			# Pad the serialization increment
			serial = '0' * (char_len - len(str(i)))
			serial += str(i)

			# Lets setup the file name for this
			file_name = prefix + '_' + str(_year) + '_' + str(month) + '_' + serial + '.csv.gz'
			
			# Lets setup the URL for this
			url = path + file_name

			# Debug purposes
			print('\nmonth: ' + colors.white + str(month) + colors.reset + ' year: ' + colors.white + str(_year) + colors.reset + ' serial: ' + colors.white + str(serial) + colors.reset +' \nfile: ' + str(file_name) + ' \nurl: ' + url)

			# Set the output file name (modify if you want a separate path rather than local)
			out_file = file_name

			# If the file doesn't exists already, grab it
			if not os.path.isfile(out_file):
				r = requests.get(url, allow_redirects=True)

				# If it is not an XML error response, write to disk!
				if '<Error>' not in r.content:
					
					# Write
					open(out_file, 'wb').write(r.content)
					print("\n Wrote file:  %s" % out_file)
				else:
					# If there was an error, let the user know
					print((colors.red + 'error in url: ' + colors.white + ' %s' + colors.reset) % url)

					#Set to true so we escape serialization
					#loop and move to increment month
					serial_error = True

			# If it does exist, increment
			else:
				print(colors.green + 'file exists: ' + colors.reset +'%s' % out_file)

			i += 1

		#reset serilization, increment month
		i=0
		serial_error = False
		_month += 1

		#reset to jan if dec and increment year
		if _month > 12:
			_month = 1
			_year += 1



print('Donesky bro. *golf clap*')

#mic drop, enter ETL-ML hell
sys.exit(0)