"""Common algorithm interviewed on that I wanted to try"""

def main():
    # creating an empty list
    array = []

    # number of elemetns as input
    n = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, n):
        ele = int(input("Enter element: "))

        array.append(ele)  # adding the element
    number = int(input("How many left rotates? "))
    result = rotate(array, number)
    return result

def rotate(array, n):

    for i in range(0,n):
        send = array.pop(0)
        array.append(send)

    return array



# driver code
print(main())