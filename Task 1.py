def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Leave non-alphabetic characters unchanged
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()

