#Date and time library
from datetime import datetime
import time

#The number of log entries a book must have
num_log_entries = int(input(''))


#If a book has 0 log entries, the program ends and gives the output
results = []
T_format = '%H:%M'
while num_log_entries != 0:
    logBook = []
    #Model of total_time_book dictionary is total_time_book = {'Night': 3600.0, 'Day': 3600.0}
    #This means logBook has 1hr in both day and night
    total_time_book = {}
    #Default is pass
    result = 'PASS'
    for i in range(0, num_log_entries):
        times = input('').split()

        sunrise = datetime.strptime(times[0], T_format)
        sunset = datetime.strptime(times[1], T_format)

        start = datetime.strptime(times[2], T_format)
        finish = datetime.strptime(times[3], T_format)

        #Journey time difference
        #a + (b - a)/2
        timeDiff = str(start + ((finish - start)/2))[11:16]

        #Time cases for result
        #Sample time:
        #             06:55 18:31 12:18 22:44 'NON'
        #             07:36 18:33 05:00 06:24 'NON'
        #             06:22 19:51 08:06 09:51 'PASS' day
        #             06:41 18:41 05:33 06:59 'PASS' night
        #             06:55 10:30 11:30 12:30 'PASS' night

        #This is to check if its less than a 2hr drive
        tdelta = datetime.strptime(times[3], T_format) - datetime.strptime(times[2], T_format)
        #print(tdelta)

        #If the drive time is greater than 2 hours, then result is 'NON'
        if(tdelta.total_seconds() > float(60*60*2)):
            result = 'NON'

        #total time book [day or night depending on which time it is] = times

        #print(datetime.strptime(timeDiff, T_format))
        if datetime.strptime(timeDiff, T_format) < sunrise or datetime.strptime(timeDiff, T_format) > sunset:
            if 'Night' not in total_time_book.keys():
                total_time_book['Night'] = float(tdelta.total_seconds())
            else:
                total_time_book['Night'] = total_time_book['Night'] + float(tdelta.total_seconds())

        elif datetime.strptime(timeDiff, T_format) > sunrise or datetime.strptime(timeDiff, T_format) < sunset:
            if 'Day' not in total_time_book.keys():
                total_time_book['Day'] = float(tdelta.total_seconds())
            else:
                total_time_book['Day'] = total_time_book['Day'] + float(tdelta.total_seconds())

        #Store a list in a list
        logBook.append(times)
    #print(total_time_book)
    if total_time_book['Night'] >= float(60 * 60 * 10) and total_time_book['Day'] >= float(60 * 60 * 40) and result != 'NON':
        result = 'PASS'
    else:
        result = 'NON'
    #Adds result once logbook is checked
    results.append(result)
    #The number of log entries a book must have
    num_log_entries = int(input(''))

for result in results:
    print(result)
