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
    data = [56, 12, 79, 23, 47, 10, 68]
    key = 47
    result = binary_search(data, key)
    print("Without sorting, result index:", result)
    data.sort()
    print("Sorted list:", data)
    result = binary_search(data, key)
    print("After sorting, result index:", result)
