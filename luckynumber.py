def has_lucky_number(nums):
    for num in nums:
        if num %7 == 0:
            return True
    
    #We've exhausted the list without finding a lucky number
        
    return False 

print(has_lucky_number([897, 121, 81, 189]))