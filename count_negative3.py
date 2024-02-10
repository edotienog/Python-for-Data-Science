def count_negatives(nums):
    #It is important to note in the booleans like True + True + False + True to be equal to 3
    return sum([num < 0 for num in nums])

print(count_negatives([-1, 9, -4, 90, -5, -3, -1]))