'''You’re on a treasure island represented as a grid. 'S' is your starting point, 'X' is dangerous water, 'O' is open land, and 'T' is the treasure. You can move up, down, left, or right. Find the minimum number of steps to reach the treasure, or -1 if it’s impossible.'''
def maxSatisfied(customers, grumpy, X):
    base_satisfied = sum(c for c, g in zip(customers, grumpy) if g == 0)
    extra = 0
    window_sum = 0

    for i in range(len(customers)):
        if grumpy[i] == 1:
            window_sum += customers[i]
        if i >= X and grumpy[i - X] == 1:
            window_sum -= customers[i - X]
        extra = max(extra, window_sum)

    return base_satisfied + extra

# Example
print(maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))  # 16
'''1'''
