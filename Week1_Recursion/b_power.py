def power(p, n):
    if n == 0:
        return 1
    return p * power(p, n - 1)


if __name__ == "__main__":
    p = 2
    n = 10
    result = power(p, n)
    print(p, "^", n, "=", result)
