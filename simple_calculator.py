# Simple Calculator Program
# This program allows the user to perform basic arithmetic operations (+, -, *, /, **, //)
# between two numbers entered via the terminal. The user selects the operation, and the
# program displays the result. Division by zero is handled gracefully.
# Note: All inputs are treated as integers.

# Prompt the user to enter the first number
x = input("Enter first number: ")

# Display the list of valid operators to the user
print("""The valid operators are as follows
      + => addition
      - => subtraction
      * => multiplication
      / => division
      ** => exponential
      // => integer division""")

# Prompt the user to enter the desired operator
operator = input("Enter operator: ")

# Prompt the user to enter the second number
y = input("Enter second number: ")

# Perform addition if operator is '+'
if (operator == "+"):
    print(f"{x} + {y} = {int(x) + int(y)}")

# Perform subtraction if operator is '-'
elif (operator == "-"):
    print(f"{x} - {y} = {int(x) - int(y)}")

# Perform multiplication if operator is '*'
elif (operator == "*"):
    print(f"{x} * {y} = {int(x) * int(y)}")

# Perform division if operator is '/' and handle division by zero
elif (operator == "/"):
    if (int(y) != 0):
        print(f"{x} / {y} = {int(x) / int(y)}")
    else:
        print("Division by zero is not possible")

# Perform exponentiation if operator is '**'
elif (operator == "**"):
    print(f"{x} ** {y} = {int(x) ** int(y)}")

# Perform integer division if operator is '//' and handle division by zero
elif (operator == "//"):
    if (int(y) != 0):
        print(f"{x} // {y} = {int(x) // int(y)}")
    else:
        print("Division by zero is not possible")

# Handle invalid operator input
else:
    print("You have entered an invalid input")
