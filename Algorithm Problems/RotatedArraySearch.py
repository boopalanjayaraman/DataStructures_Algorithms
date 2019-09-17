def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # rotated array search (or pivoted array search) can be solved in the following way.
    # 1. Find the pivot
    # 2. Split the array now into two on the pivot and run binary searches on the two sub-arrays.
    # 3. Use binary search to find pivot, Pivot is the only point where an element will be less than its previous element
    pivot_index = find_pivot(input_list, 0, len(input_list)-1)

   # if pivot is not found, array is not rotated

    if pivot_index == -1:
        search_index = binary_search(input_list, number, 0, len(input_list) - 1)
        return search_index

    # if pivot is found, check the pivot first, and then run binary search on split sub arrays.
    if input_list[pivot_index] == number:
        return pivot_index
    elif input_list[0] <= number:
        search_index = binary_search(input_list, number, 0, pivot_index - 1)
        return search_index
    else:
        search_index = binary_search(input_list, number, pivot_index + 1, len(input_list) - 1)
        return search_index

    
def binary_search(input_list, value, start, end):
    if start > end:
        return -1
    #if start == end:
    #    return start

    middle = (start + end)// 2
    middle_value = input_list[middle]

    if(middle_value == value):
        return middle
    elif middle_value < value:
        return binary_search(input_list, value, middle + 1, end)
    else:
        return binary_search(input_list, value, start, middle - 1)

def find_pivot(input_list, start, end):
    if start > end:
        return -1
    if start == end:
        return start
    
    middle = (start + end)//2
    middle_value = input_list[middle]

    if middle < end and middle_value > input_list[middle + 1]:
        return middle
    elif middle > start and input_list[middle - 1] > middle_value:
        return middle - 1
    elif input_list[start] >= input_list[middle]:
        return find_pivot(input_list, start, middle - 1) 

    return find_pivot(input_list, middle + 1, end)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #pass
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #pass
    test_function([[6, 7, 8, 1, 2, 3, 4], 8]) #pass
    test_function([[6, 7, 8, 1, 2, 3, 4], 1]) #pass
    test_function([[6, 7, 8, 1, 2, 3, 4], 10]) #pass

    #additional test cases
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4]) #pass
    test_function([[4, 3, 2, 1], 2]) #pass
    test_function([[1], 1]) #pass
    test_function([[1, 2, 3, 4, 5], 3]) #pass
    test_function([[1, 2, 3, 4, 5], 1]) #pass
    test_function([[1, 2, 3, 4, 5], 5]) #pass
