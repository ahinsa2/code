def sum_of_n(n):
    if n == 0:
        return 0
    return n + sum_of_n(n - 1)

# Example
n = 5
print("Sum of first", n, "numbers:", sum_of_n(n))
