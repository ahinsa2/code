def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

# Example
print(is_anagram("listen", "silent"))
