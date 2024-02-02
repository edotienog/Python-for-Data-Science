def round_of_to_nearest100(num):
    return round(num, -2) #Here negative -1 rep 10, while -2 rep 100, 3 rep 1000 and so on

print(round_of_to_nearest100(4397891))