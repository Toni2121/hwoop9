def count_occurrences(lst, val, index=0):
    if index == len(lst):
        return 0
    count_rest = count_occurrences(lst, val, index + 1)
    return (1 if lst[index] == val else 0) + count_rest


if __name__ == "__main__":
    print(count_occurrences([1, 2, 2, 3, 2, 4], 2))
    print(count_occurrences([5, 5, 5, 5], 5))
    print(count_occurrences([1, 2, 3, 4], 6))
