def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    current_number = 0
    for number in numbers:
        if number > current_number:
            current_number = number

    
    return current_number


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
