def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #sort the list first
    quick_sort(input_list, 0, len(input_list) - 1)

    #print('sorted array: ', input_list)
    number1 = ''
    number2 = ''

    #pick digits from the array in reverse order alternatively
    for index in range(len(input_list) - 1, -1, -1):
        if index % 2 ==0:
            number1 += str(input_list[index])
        else:
            number2 += str(input_list[index])

    return int(number1), int(number2)

def quick_sort(input_list, start, end):
    if start < end:
        pivot_value = input_list[start]
        left = start
        right = end

        while left <= right:
            #loop until we find a number that is more than pivot's value, on the left side
            while input_list[left] < pivot_value:
                left += 1

            #loop until we find a number that is less than pivot's value, on the right side
            while input_list[right] > pivot_value:
                right -= 1

            #swap both of them
            if left <= right:
                temp = input_list[left]
                input_list[left] = input_list[right]
                input_list[right] = temp
                # move positions by one
                left += 1
                right -= 1

        quick_sort(input_list, start, right) # right became less than left
        quick_sort(input_list, left, end) # left became greater than right
            



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail - ", output)

if __name__ == "__main__":
    test_function([[1, 2, 3, 4, 5], [542, 31]]) #prints pass
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) #prints pass
    test_function([[0, 1], [1, 0]]) #prints pass
    test_function([[1, 2, 3], [31, 2]]) #prints pass
    test_function([[0, 2, 3, 9, 4, 5, 8, 6, 7], [97530, 8642]]) #prints pass
