s = input("Enter a string: ")
i = 0
print("Forward direction:")
while i < len(s):
    print(s[i], end=" ")
    i += 1

print("\nBackward direction:")
i = len(s) - 1
while i >= 0:
    print(s[i], end=" ")
    i -= 1
