import os


def push(stack, element, size):
    """Push an element to the stack."""
    if is_full(stack, size):
        print("Stack is full, cannot push element.")
    else:
        stack.append(element)
        print(f"Element {element} pushed to the stack.")


def pop(stack):
    """Pop an element from the stack."""
    if is_empty(stack):
        print("Stack is empty, cannot pop element.")
    else:
        print(f"Element {stack.pop()} popped from the stack.")


def is_empty(stack):
    """Check if the stack is empty."""
    return len(stack) == 0


def is_full(stack, size):
    """Check if the stack is full."""
    return len(stack) == size


def top(stack):
    """Return the top element of the stack."""
    if is_empty(stack):
        print("Stack is empty, no top element.")
    else:
        print(f"Top element of the stack is {stack[-1]}")


def main():
    stack = []
    size = int(input("Enter the size of the stack: "))

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Check if Empty")
        print("4. Check if Full")
        print("5. Top")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        os.system("clear")

        if choice == 1:
            element = int(input("Enter the element to push: "))
            push(stack, element, size)
        elif choice == 2:
            pop(stack)
        elif choice == 3:
            print("Stack is empty." if is_empty(stack) else "Stack is not empty.")
        elif choice == 4:
            print("Stack is full." if is_full(stack, size) else "Stack is not full.")
        elif choice == 5:
            top(stack)
        elif choice == 6:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, Please try again...")


if __name__ == "__main__":
    main()
