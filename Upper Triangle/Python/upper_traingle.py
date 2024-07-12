def print_upper_triangle(n):
    # Print the upper triangle pattern
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Example usage
n = 3
print_upper_triangle(n)
