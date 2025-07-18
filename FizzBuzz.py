#FizzBuzz Program in Python
#This program prints numbers from 1 up to a user-specified limit.
#For each number in that range:
# If it is divisible by 3, it prints "Fizz"
# If it is divisible by 5, it prints "Buzz"
# If it is divisible by both 3 and 5, it prints "FizzBuzz"
# Otherwise, it prints the number itself

def fizz_buzz(highest_number):
    # Loop through numbers from 1 up to  highest_number
    for number in range(1, highest_number + 1):
        # If number is divisible by 3, print "Fizz"
        if (number % 3 == 0):
            print("Fizz")
        # If number is divisible by 5, print "Buzz"
        elif (number % 5 == 0):
            print("Buzz")
        # If number is divisible by both 3 and 5, print "FizzBuzz"
        elif (number % 15 == 0):
            print("FizzBuzz")
        # Otherwise, print the number itself
        else:
            print(number)


# Get user input for the highest number to check
highest_number = input("highest number: ")
# Call the fizz_buzz function, converting input to an integer
fizz_buzz(int(highest_number))
