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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def get_unique_numbers(data_list):
    numbers_0 = [record[0] for record in data_list]
    numbers_1 = [record[1] for record in data_list]
    numbers_0.extend(numbers_1)
    unique_numbers = set(numbers_0)
    return unique_numbers


if __name__ == '__main__':
    all_unique_numbers = get_unique_numbers(texts)
    all_unique_numbers.update(get_unique_numbers(calls))
    print('There are {0} different telephone numbers in the records.'.format(len(all_unique_numbers)))