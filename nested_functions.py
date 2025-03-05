# Define a function to calculate the square of a number
def square(num):
    """Returns the square of the given number."""
    return num * num  # Or num ** 2

# Define a function to calculate the sum of squares
def sum_of_squares(numbers):
    """Returns the sum of the squares of the numbers in the list."""
    total = 0
    for n in numbers:
        total += square(n)  # Call the square function and add to total
    return total

# Define a list of numbers
numbers_list = [2, 3, 4]

# Call the sum_of_squares function and store the result
result = sum_of_squares(numbers_list)

# Print the final result
print(f"The sum of squares is: {result}")
