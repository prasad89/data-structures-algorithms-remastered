import os


def enqueue(queue, element, size):
    """Add an element to the queue."""
    if is_full(queue, size):
        print("Queue is full, cannot enqueue element.")
    else:
        queue.append(element)
        print(f"Element {element} enqueued to the queue.")


def dequeue(queue):
    """Remove an element from the queue."""
    if is_empty(queue):
        print("Queue is empty, cannot dequeue element.")
    else:
        print(f"Element {queue.pop(0)} dequeued from the queue.")


def is_empty(queue):
    """Check if the queue is empty."""
    return len(queue) == 0


def is_full(queue, size):
    """Check if the queue is full."""
    return len(queue) == size


def front(queue):
    """Get the front element of the queue."""
    if is_empty(queue):
        print("Queue is empty, no front element.")
    else:
        print(f"Front element of the queue is {queue[0]}")


def rear(queue):
    """Get the rear element of the queue."""
    if is_empty(queue):
        print("Queue is empty, no rear element.")
    else:
        print(f"Rear element of the queue is {queue[-1]}")


def main():
    queue = []
    size = int(input("Enter the size of the queue: "))

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Check if Empty")
        print("4. Check if Full")
        print("5. Front")
        print("6. Rear")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        os.system("clear")

        if choice == 1:
            element = int(input("Enter the element to enqueue: "))
            enqueue(queue, element, size)
        elif choice == 2:
            dequeue(queue)
        elif choice == 3:
            print("Queue is empty." if is_empty(queue) else "Queue is not empty.")
        elif choice == 4:
            print("Queue is full." if is_full(queue, size) else "Queue is not full.")
        elif choice == 5:
            front(queue)
        elif choice == 6:
            rear(queue)
        elif choice == 7:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, Please try again...")


if __name__ == "__main__":
    main()
