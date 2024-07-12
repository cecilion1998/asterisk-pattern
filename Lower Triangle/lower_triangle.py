def print_inverted_centered_triangle(n):
    # Print the inverted centered triangle pattern
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Example usage
n = 3
print_inverted_centered_triangle(n)