def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


if __name__ == "__main__":
    print(sum_digits(86))
    print(sum_digits(404))
