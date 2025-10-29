def linear_search(arr, key):
    for i, val in enumerate(arr):
        if val == key:
            return i
    return -1

nums = [4, 7, 2, 9, 1]
key = int(input("Enter key: "))
print("Found at index:", linear_search(nums, key))
