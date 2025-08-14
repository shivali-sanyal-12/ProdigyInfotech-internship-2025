def caesar_cipher(text, shift, encrypt=True):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if encrypt:
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char

    return result

# Main program
while True:
    choice = input("Encrypt or Decrypt? (e/d): ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Try again.")
        continue

    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'e':
        print("Encrypted:", caesar_cipher(message, shift))
    else:
        print("Decrypted:", caesar_cipher(message, shift, encrypt=False))

    again = input("Try again? (yes/no): ").lower()
    if again != 'yes':
        break
