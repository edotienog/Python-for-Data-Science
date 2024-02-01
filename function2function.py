def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """call fn or arg"""
    return fn(arg)

def squared_call(fn, arg):
    """call fn on the resutl of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep = '\n' #Print the results in a new line
)