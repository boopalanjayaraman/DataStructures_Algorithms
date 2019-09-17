import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    max = ints[0]
    min = ints[0]

    for number in ints:
        if number < min:
            min = number
        if number > max:
            max = number
    return (min, max)

if __name__ == "__main__":
    ## Example Test Case of Ten Integers

    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") #Pass

    l = [i for i in range(10, 200)]  # a list containing 10 - 199
    random.shuffle(l)

    print ("Pass" if ((10, 199) == get_min_max(l)) else "Fail") #Pass

    l = [i for i in range(8, 99)]  # a list containing 8 - 98
    random.shuffle(l)

    print ("Pass" if ((8, 98) == get_min_max(l)) else "Fail") #Pass

    l = [i for i in range(0, 1)]  # a list containing 0 - 0
    random.shuffle(l)

    print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail") #Pass