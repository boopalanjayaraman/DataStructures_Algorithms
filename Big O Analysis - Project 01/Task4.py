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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

if __name__ == '__main__':
    callers = set()
    receivers = set()

    text_senders = set()
    text_receivers = set()

    for call_record in calls:
        callers.add(call_record[0])
        receivers.add(call_record[1])

    for text_record in texts:
        text_senders.add(text_record[0])
        text_receivers.add(text_record[1])

    telemarketers = []
    print('These numbers could be telemarketers: ')
    for caller in sorted(callers):
        if ((caller in receivers) == False) & ((caller in text_senders) == False) & ((caller in text_receivers) == False):
             telemarketers.append(caller)
             print(caller)
    