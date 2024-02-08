def select_second(L):
    """Returns the second element of the given list. If the el
    the list has no second element, return None"""
    if len(L)>= 2:
        return L[1]
    else: 
        return None
    
print(select_second(["Kenya", "Ghana", "Sweden", "Poland", ]))
