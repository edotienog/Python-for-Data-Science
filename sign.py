def sign(int):
    if int < 0:
        return -1
    elif int > 0:
        return 1
    else:
        return 0
    
print(sign(98))
print(sign(-1))