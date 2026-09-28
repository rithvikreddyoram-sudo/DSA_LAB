def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    data = [10, 23, 35, 47, 56, 68, 79]
    key = 47
    result = binary_search(data, key)
    if result != -1:
        print("Element", key, "found at index", result)
    else:
        print("Element", key, "not found")
