# Define a list of 15 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Loop through the list and check if each number is even or odd
for number in numbers:
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
