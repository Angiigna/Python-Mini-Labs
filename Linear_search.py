# 🔍 Linear Search Program
# This program takes a list of numbers from the user and searches for a specific item using linear search.
# It checks each element in the list one by one until it finds the target or reaches the end of the list.
# If found, it prints the index of the item; otherwise, it prints "Item not in list".


def linear_search(numbers, item):
    # Loop through each number in the list with its index
    for index, number in enumerate(numbers):
        # If the current number matches the item, print its index and exit loop
        if number == item:
            print(f"item found at index {index} ")
            break
    else:
        # If loop completes without finding the item, print not found message
        print("Item not in list")


# Read a list of numbers from user input, split by spaces
numbersstr = input("Enter your list: ")
numbers = list(map(int, numbersstr.split(" ")))
print(numbers)  # Print the list for confirmation
# Read the item to search for
item = int(input("Enter the search item: "))
# Call the linear search function
linear_search(numbers, item)
