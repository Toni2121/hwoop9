def print_range_recursive(start, jump, final):
    max_val = start
    while max_val + jump <= final:
        max_val += jump

    def helper(num):
        if num < start:
            return
        print(num, end=" ")
        helper(num - jump)

    helper(max_val)
    print()


if __name__ == "__main__":
    print_range_recursive(8, 3, 15)
