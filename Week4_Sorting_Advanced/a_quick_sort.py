def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


if __name__ == "__main__":
    data = [10, 80, 30, 90, 40, 50, 70]
    print("Before sorting:", data)
    quick_sort(data, 0, len(data) - 1)
    print("After sorting:", data)
