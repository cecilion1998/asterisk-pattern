def print_left_aligned_diamond(n):
    # Print the upper part of the diamond
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (i + 1))

    # Print the lower part of the diamond
    for i in range(n - 1):
        print(' ' * (i + 1) + '*' * (n - i - 1))


# Example usage
n = 3
print_left_aligned_diamond(n)
