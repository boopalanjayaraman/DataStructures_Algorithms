def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number

    if number < 0:
        return None

    start = 0
    end = number // 2
    result = 0

    while start <= end:
        middle = (start + end) // 2
        squared_middle = middle * middle

        if squared_middle == number:
            return middle 
        elif squared_middle < number:
            start = middle + 1
            result = middle
        else:
            end = middle - 1
        
    return result

if __name__ == "__main__":
    print ("Pass" if  (3 == sqrt(9)) else "Fail")
    print ("Pass" if  (0 == sqrt(0)) else "Fail")
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    print ("Pass" if  (1 == sqrt(1)) else "Fail")
    print ("Pass" if  (5 == sqrt(27)) else "Fail")

    #additional test cases
    print ("Pass" if  (None == sqrt(-10)) else "Fail")
    print ("Pass" if  (12 == sqrt(144)) else "Fail")
    print ("Pass" if  (25 == sqrt(625)) else "Fail")

    #print
    print(sqrt(10000))
    print(sqrt(1000))
    print(sqrt(99))