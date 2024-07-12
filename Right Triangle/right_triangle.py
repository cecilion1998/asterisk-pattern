def print_pattern(n):
    # Print the upper part of the pattern
    for i in range(1, n + 1):
        print('*' * i)

    # Print the lower part of the pattern
    for i in range(n - 1, 0, -1):
        print('*' * i)


# Example usage
n = 3
print_pattern(n)