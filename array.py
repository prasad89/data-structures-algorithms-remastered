import os

def insert(arr, target, position):
    """Insert an element into the array."""
    arr.insert(position, target)
    print(f"Element {target} inserted at index {position}")
    display(arr)

def display(arr):
    """Display the elements of the array."""
    for i in range(len(arr)):
        print(f"Element at index {i} is {arr[i]}")


def delete(arr, target):
    """Delete an element from the array."""
    position = find_index(arr, target)
    if position == -1:
        print(f"Element {target} not found in the array")
        return

    for i in range(position, len(arr) - 1):
        arr[i] = arr[i + 1]

    arr.pop()
    print(f"Element {target} deleted from the array.")
    display(arr)


def search(arr, target):
    """Search for an element in the array."""
    position = find_index(arr, target)
    if position == -1:
        print(f"Element {target} not found in the array")
    else:
        print(f"Element {target} found at index {position}")


def update(arr, old_val, new_val):
    """Update an element in the array."""
    position = find_index(arr, old_val)
    if position == -1:
        print(f"Element {old_val} not found in the array")
    else:
        arr[position] = new_val
        print(f"Element {old_val} updated to {new_val} at index {position}")
        display(arr)


def find_index(arr, target):
    """Find the index of the target element in the array."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def clear_screen():
    """Clear the terminal screen."""
    os.system("clear")


def main():
    arr = [1, 2, 3, 4, 5]

    while True:
        print("Array Operations:")
        print("1. Insert")
        print("2. Display")
        print("3. Delete")
        print("4. Search")
        print("5. Update")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            clear_screen()
            target = int(input("Enter the element to insert: "))
            position = int(input("Enter the position to insert: "))
            insert(arr, target, position)
        elif choice == 2:
            clear_screen()
            display(arr)
        elif choice == 3:
            clear_screen()
            target = int(input("Enter the element to delete: "))
            delete(arr, target)
        elif choice == 4:
            clear_screen()
            target = int(input("Enter the element to search: "))
            search(arr, target)
        elif choice == 5:
            clear_screen()
            old_val = int(input("Enter the element to update: "))
            new_val = int(input("Enter the new element: "))
            update(arr, old_val, new_val)
        elif choice == 6:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, Please try again...")


if __name__ == "__main__":
    main()
