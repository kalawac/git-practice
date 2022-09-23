def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    
    num_max = numbers[0]
    for num in numbers:
        if num > num_max:
            num_max = num
        else:
            continue
    return num_max



if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
