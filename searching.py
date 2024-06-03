def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"{target} found at index {i} in the array")
            return
    print(f"{target} not found in the array")
    return


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:

        if arr[mid] == target:
            print(f"{target} found at index {mid} in the array")
            return
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"{target} not found in the array")
    return


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    target = int(input("Enter the number to search: "))

    choice = (
        input("Enter the search algorithm to use (linear/binary): ").strip().lower()
    )

    if choice == "linear":
        linear_search(arr, target)
    elif choice == "binary":
        binary_search(arr, target)
    else:
        print("Invalid choice")
        return


if __name__ == "__main__":
    main()
