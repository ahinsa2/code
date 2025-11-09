# Accept a string from the user
s = input("Enter a string: ")

# Display using positive index
print("Characters by positive index:")
for i in range(len(s)):
    print(f"Index {i} → {s[i]}")

# Display using negative index
print("\nCharacters by negative index:")
for i in range(-1, -len(s)-1, -1):
    print(f"Index {i} → {s[i]}")
