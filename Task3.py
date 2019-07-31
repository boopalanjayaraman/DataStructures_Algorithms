"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
from collections import defaultdict
import re

if __name__ == '__main__':
  area_codes = defaultdict(int)

  area_code_format = r'(\([0-9]*\))[0-9]*'
  mobile_format = r'([7|8|9][0-9]*)\s[0-9]*'

  for call_record in calls:
    caller = call_record[0]
    if caller.startswith('(080)'):
      receiver = call_record[1]
      #see if the receiver was a landline phone by checking for area code
      match_area_code = re.search(area_code_format, receiver)
      if (match_area_code != None):
        area_code_with_brackets = match_area_code.groups(0)[0]
        area_code = area_code_with_brackets[1:len(area_code_with_brackets)-1]
        area_codes[area_code] += 1
        continue

      #see if the receiver was a mobile number by checking for mobile number format
      match_mobile_code = re.search(mobile_format, receiver)
      if(match_mobile_code != None):
        mobile_code = match_mobile_code.groups(0)[0][0:4]
        area_codes[mobile_code] += 1
        continue

  print('The numbers called by people in Bangalore have codes:')
  for code in sorted(area_codes.keys()):
    print(code)
  
  total_calls_made_from_080 = sum([val for key, val in area_codes.items()])
  calls_made_to_080 = area_codes['080']

  print('{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(total_calls_made_from_080/calls_made_to_080))
  

