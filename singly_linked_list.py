class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def create(arr):
    """Create a singly linked list from an array."""
    head = Node(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head


def get_node_at(head, position):
    """Return the node at a specific position (1-based index)."""    
    current = head
    for _ in range(position - 1):
        if current is None:
            return None
        current = current.next
    return current


def insert(head, target, position):
    """Insert an element at a given position in the linked list."""
    if position < 1:
        print("Invalid position")
        return head

    new_node = Node(target)
    if position == 1:
        new_node.next = head
        return new_node

    prev = get_node_at(head, position - 1)
    if prev is None:
        print("Invalid position")
        return head

    new_node.next = prev.next
    prev.next = new_node
    return head


def display(head):
    """Display the linked list."""
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def delete(head, target):
    """Delete a target value from the linked list."""
    if head.data == target:
        print(f"Element {target} deleted from the linked list")
        return head.next

    current = head
    while current.next:
        if current.next.data == target:
            current.next = current.next.next
            print(f"Element {target} deleted from the linked list")
            return head
        current = current.next
    print(f"Element {target} not found in the linked list")
    return head


def search(head, target):
    """Search for a target value in the linked list and return its position."""
    current = head
    position = 1
    while current:
        if current.data == target:
            print(f"Element {target} found at position {position}")
            return position
        current = current.next
        position += 1
    print(f"Element {target} not found")
    return None


def update(head, old_val, new_val):
    """Update a value in the linked list."""
    current = head
    while current:
        if current.data == old_val:
            current.data = new_val
            print(f"Element {old_val} updated to {new_val}")
            return head
        current = current.next
    print(f"Element {old_val} not found in the linked list")
    return head


def clear_screen():
    """Clear the terminal screen."""
    import os

    os.system("clear")


def main():
    arr = [1, 2, 3, 4, 5]
    head = create(arr)

    while True:
        print("Linked List Operations:")
        print("1. Insert")
        print("2. Display")
        print("3. Delete")
        print("4. Search")
        print("5. Update")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        clear_screen()

        if choice == 1:
            target = int(input("Enter the element to insert: "))
            position = int(input("Enter the position to insert: "))
            head = insert(head, target, position)
        elif choice == 2:
            display(head)
        elif choice == 3:
            target = int(input("Enter the element to delete: "))
            head = delete(head, target)
        elif choice == 4:
            target = int(input("Enter the element to search: "))
            search(head, target)
        elif choice == 5:
            old_val = int(input("Enter the element to update: "))
            new_val = int(input("Enter the new element: "))
            head = update(head, old_val, new_val)
        elif choice == 6:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, Please try again...")


if __name__ == "__main__":
    main()
