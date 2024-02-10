def count_negative(nums):
    return len([num for num in nums if num <0])

print(count_negative([-5, 1, -2, 0, -1, 0]))