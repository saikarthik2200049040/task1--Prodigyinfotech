def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shifted = ord(char) + shift if mode == "encrypt" else ord(char) - shift
            if char.islower():
                if mode == "encrypt":
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                else:
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
            elif char.isupper():
                if mode == "encrypt":
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                else:
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

# Get input from user
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
choice = input("Encrypt or Decrypt? (Type 'encrypt' or 'decrypt'): ")

# Validate user's choice
if choice.lower() == "encrypt":
    encrypted_text = caesar_cipher(text, shift, "encrypt")
    print("Encrypted text:", encrypted_text)
elif choice.lower() == "decrypt":
    decrypted_text = caesar_cipher(text, shift, "decrypt")
    print("Decrypted text:", decrypted_text)
else:
    print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
