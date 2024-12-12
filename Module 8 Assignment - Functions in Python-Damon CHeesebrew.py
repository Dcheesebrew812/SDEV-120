# Define the function
def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False

# Main section of the program
a = 2
b = 3
result = greaterThan(a, b)

# Print the output
print("The statement", str(a), "is greater than", str(b), "is", str(result))

# Test with different values
a = 10
b = 6
result = greaterThan(a, b)

# Print the output
print("The statement", str(a), "is greater than", str(b), "is", str(result))
