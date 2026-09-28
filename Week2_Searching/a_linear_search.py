def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    data = [45, 12, 78, 23, 56, 89]
    key = 23
    result = linear_search(data, key)
    if result != -1:
        print("Element", key, "found at index", result)
    else:
        print("Element", key, "not found")
