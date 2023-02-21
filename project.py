import re
import sys


def main():
    # Get user's email and validate it
    email = input("Enter your email: ")
    while not is_valid_email(email):
        print("Invalid email format!")
        email = input("Enter your email: ")

    # Get user's password and check if it's strong
    password = input("Enter a password: ")
    while not is_strong_password(password):
        print("Password is not strong enough! Must contain at least 8 characters, one uppercase letter, one lowercase letter, one digit and one special character.")
        password = input("Enter a password: ")

    while True:
        print("\nAvailable operations:")
        print("1.Encrypt a message     2.Decrypt a message    3.Exit\n")
        val = input("Enter your choice: ")
        match val:
            case "1":
        # Encrypt a message using the user's password as the key
                Emessage = input("\nEnter a message to encrypt: ")
                encrypted_message = encrypt(Emessage, len(password))
        # Write the encrypted message to a file
                with open("encrypted_message.txt","a") as file:
                    file.write(encrypted_message)
                    file.write("\n")
            case "2":
                Dmessage = input("\nEnter a message to decrypt: ")
                decrypted_message = decrypt(Dmessage, len(password))
                with open("decrypted_message.txt","a") as file:
                    file.write(decrypted_message)
                    file.write("\n")
            case "3":
                sys.exit("Exited")
            case _:
                print("\"Invalid Input!\"")


# Function to validate email format
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)


# Function to check if a password is strong
def is_strong_password(password):
    # Password must be at least 8 characters long, and contain at least one uppercase letter,
    # one lowercase letter, one digit and one special character
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d@$!%*#?&_]{8,}$"
    return re.match(pattern, password)


# Function to encrypt a message using a simple Caesar cipher
def encrypt(Emessage, key):
    encrypted_message = ""
    for char in Emessage:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) + key - 65) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message


def decrypt(Dmessage, key):
    decrypted_message = ""
    for char in Dmessage:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - key - 65) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - key - 97) % 26 + 97)
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message


if __name__ == '__main__':
    main()