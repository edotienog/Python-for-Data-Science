def mod_5(x):
    """Returns the remainder of x after dividing by 5"""
    return x % 5

print(
    "which number is biggest?",
      max(100, 51, 14),
    "which number is the biggest modulo 5?",
        max (100, 51, 14, key = mod_5),
        sep = '\n'
)