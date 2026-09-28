def search(ids, key, index):
    if index == len(ids):
        return -1
    if ids[index] == key:
        return index
    return search(ids, key, index + 1)


if __name__ == "__main__":
    employees = [101, 105, 110, 120, 135]
    key = 120
    pos = search(employees, key, 0)
    if pos == -1:
        print("Employee ID", key, "not found")
    else:
        print("Employee ID", key, "found at index", pos)
