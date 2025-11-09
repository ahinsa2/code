s = input("Enter a message to encrypt: ")
encrypted = ""

for ch in s:
    if ch.isalpha():
        shift = 3
        if ch.islower():
            encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
    else:
        encrypted += ch

print("Encrypted message:", encrypted)
