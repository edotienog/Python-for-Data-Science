def count_negative(nums):
    """" Return the number of negative in the given list 
    >>>count_negative ([5, -1, -2, 0, 3])
     """
    n_negative = 0
    for num in nums: 
        if num < 0:
            n_negative = n_negative + 1

    return n_negative
nums_list = [5, -1, -2, 0, 3]
num_negative = count_negative = (nums_list)
print(num_negative)