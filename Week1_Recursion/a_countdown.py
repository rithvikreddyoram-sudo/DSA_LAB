def countdown(n):
    if n == 0:
        print("Launch!")
        return
    print(n)
    countdown(n - 1)


if __name__ == "__main__":
    n = 5
    countdown(n)
