def to_smash(total_candies, num_friends =3):
    """Return the number of leftover candies that must be 
    smashed after distributing 
    the given number of candies evenly between a given number of friends
    if no second argument is provided, it will assume 3 friends as before
    >>> to_smash(91)
    1
    >>> to_smash(91, 4)
    """
    if total_candies == 1:
        print("Splitting 1 candy")
    else: 
        print("Splitting", total_candies, "candiesu")
    return total_candies % num_friends

print(to_smash(91, 4))
print(to_smash(1))