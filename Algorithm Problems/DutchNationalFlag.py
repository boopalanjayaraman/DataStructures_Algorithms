def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start = 0
    end = len(input_list) - 1

    left = start
    next_index_for_2 = end
    next_index_for_0 = 0

    while left <= next_index_for_2:
        # see if the number is more than pivot's value, on the left side. Do a swap if so.
        if input_list[left] == 0:
            input_list[left], input_list[next_index_for_0] = input_list[next_index_for_0], input_list[left]
            next_index_for_0 += 1
            left += 1
        # see if the number is less than pivot's value, on the right side. Do a swap if so.
        elif input_list[left] == 2:
            input_list[left], input_list[next_index_for_2] = input_list[next_index_for_2], input_list[left]
            next_index_for_2 -= 1
            #do not increment left here it could hold 0/1
        else :
            left += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])  #prints [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2], Pass
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) #prints [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],Pass
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) #prints [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],Pass
    test_function([1, 1, 1, 1, 2, 1, 1, 2, 0, 0, 0]) #prints [0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2],Pass
    test_function([0]) #prints [0],Pass
    test_function([]) #prints [],Pass
    test_function([1]) #prints [1],Pass
    test_function([2]) #prints [2],Pass