# CAESAR CIPHER MESSAGE ENCRYPTION AND DECRYPTION
#### Video Demo:  https://youtu.be/8HG8_FwQL8k
#### Description:
    This project is aimed at developing a Python program that implements a simple encryption and decryption technique using the Caesar Cipher method. This method involves shifting the letters of the message by a certain number of positions to the right or left, thereby creating a new encrypted message. The same technique is used to decrypt the message by shifting the letters back to their original positions
    In cryptography, the caesar cipher is one of the simplest and most widely known encryption techniques.

    This encryption technique is used to encrypt plain text, and to encrypt data, we have to replace each letter in the text with some other letter at a fixed difference.

    The program will consist of several functions that perform various tasks related to encryption and decryption. The functions will be defined at the same indentation level as the main function and will include:
    1. 'encrypt(message, shift)' - This function will take a message and a shift value as input and return an encrypted message. The message can be any string of characters and the shift value will be an integer value that represents the number of positions to shift the letters.
    2. 'is_valid_email(email)' - This function will take an email address as input and will return a Boolean value that indicates whether the email is valid or not. It will use regular expressions to check whether the email follows the standard format of an email address.
    3. 'is_strong_password(password)' - This function will take a password as input and will return a Boolean value that indicates whether the password is strong or not. A strong password will contain a mix of uppercase and lowercase letters, numbers, and special characters.
    4. 'decrypt(message, shift)' - This function will take an encrypted message and a shift value as input and will return the original message. It will use the same shifting technique as the 'encrypt' function to reverse the encryption process.

    The program will also use exception handling to handle errors that may occur during execution, such as invalid inputs or file errors. It will also use file I/O to store and retrieve the encrypted messages.

    Finally, the project will be tested using the assert keyword and pytest library to ensure that the functions are working correctly and returning the expected output.

    Overall, this project will provide a simple yet effective method of encrypting and decrypting messages using the Caesar Cipher method, and will showcase the use of various Python features such as functions, regular expressions, file I/O, and exception handling.


    This is CS50!
