# This program performs a Binary Search on a user-provided list of integers.
# It first sorts the list, then recursively searches for the given item by 
# dividing the list in half each time, reducing the search space efficiently.
# If the item is found, its index is printed; otherwise, the program informs
# the user that the item is not in the list.


def binary_search(numbers, item, lower_index, upper_index):
    # Base case: if lower index exceeds upper index, item is not in the list
    if lower_index > upper_index:
        print("Item not in list")
        return
    else:
        # Calculate the middle index
        mid_index = (lower_index + upper_index) // 2
        mid_value = numbers[mid_index]  # Get the value at the middle index
        # If the item matches the middle value, print its index
        if item == mid_value:
            print(f"Item found at index {mid_index} in the sorted list")
        # If the item is less than the middle value, search the left half
        elif item < mid_value:
            binary_search(numbers, item, lower_index, mid_index - 1)
        # If the item is greater than the middle value, search the right half
        else:
            binary_search(numbers, item, mid_index + 1, upper_index)


# Read a list of integers from user input and split by spaces
numbers = list(
    map(int, input("Enter your list with space between numbers: ").split(" ")))
# Read the item to search for
item = int(input("Enter the search item: "))
numbers.sort()  # Sort the list before performing binary search
# Call the binary search function with initial indices
binary_search(numbers, item, 0, len(numbers) - 1)
