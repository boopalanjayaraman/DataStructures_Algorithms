"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from collections import defaultdict

if __name__ == '__main__':
    #The whole data of calls are actually for September 2016, 
    #And hence it does not need to be filtered for time period. Process the whole file.
    #Get a mapping between number and their time

    caller_col_index = 0
    receiver_col_index = 1
    time_col_index = 3

    phone_usage = defaultdict(int) #key:  phone_number, val: time
    for call_record in calls:
        phone_usage[call_record[caller_col_index]] += int(call_record[time_col_index])
        phone_usage[call_record[receiver_col_index]] += int(call_record[time_col_index])

    longest_time_duration = 0
    high_usage_number = ''
    for key, val in phone_usage.items():
        if val > longest_time_duration:
            longest_time_duration = val
            high_usage_number = key
            
    print('{0} spent the longest time, {1} seconds, on the phone during September 2016.'.format(high_usage_number, longest_time_duration))