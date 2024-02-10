def count_negatives(num):
    """Return the number of negative in given
    list 
    >>>count_negative([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in num:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative
print(count_negatives([5, -1, -2, 0, 3]))