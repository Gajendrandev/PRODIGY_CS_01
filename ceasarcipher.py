def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("Select an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
