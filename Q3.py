import re

s = input("Enter a string containing numbers: ")
numbers = re.findall(r'\d+', s)  # Find all numbers
numbers = list(map(int, numbers))  # Convert to integers
print("Numbers found:", numbers)
print("Sum of numbers:", sum(numbers))
