a = [1, 2, 3]
b = [3, 2, 1]

# Introduce a new variable to temporarily store one of the old value
tmp = a 

a = b
b = tmp

print(a)
print(b)