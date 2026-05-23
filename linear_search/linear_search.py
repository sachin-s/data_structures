def linear_search(array, id):
    """
    linear_search(array, id) takes two argument => array and id,
    and searches the id in the array and returns the index at
    which the element is present, else returns -1 if element is not found
    """

    for index in range(len(array)):
        if array[index] == id:
            return index

    return -1


numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 30))  # Output: 2
print(linear_search(numbers, 99))  # Output: -1