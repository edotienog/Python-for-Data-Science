# Define a function called parse that takes a list of numbers as an argument
def parse(numbers):
    # Create an empty list to store the results
    results = []
    # Loop through each number in the list
    for number in numbers:
        # Add 2 to the number and append it to the results list
        results.append(number + 2)
    # Return the results list
    return results

# Create a list of numbers
numbers = [1, 2, 3]
# Call the parse function with the numbers list and assign the output to a variable called squared
squared = parse(numbers)
# Print the value of squared
print(squared)
