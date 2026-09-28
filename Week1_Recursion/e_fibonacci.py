def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    n = 8
    print("Fibonacci series:")
    for i in range(n):
        print(fib(i), end=" ")
    print()
