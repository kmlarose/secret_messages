from affine import Affine
from alberti import Alberti
from atbash import Atbash
from caesar import Caesar
import os


def clear():
    """Clears text off the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def run_console_ui():
    """
    Runs the console user interface
    Allows the user to encrypt or decrypt a message,
    and to select which kind of cipher to use
    """
    main_menu = [
        '1: Encrypt a Message',
        '2: Decrypt a Message',
        'Q: Quit']
    cipher_menu = [
        '1: Caesar Cipher',
        '2: Alberti Cipher',
        '3: Affine Cipher',
        '4: Atbash Cipher',
        'B: Back to Main Menu',
        'Q: Quit']
    # TODO-kml: add some kind of help option to explain what the heck is going on here
    # TODO-kml: get the user inputs required to set up your ciphers
    # TODO-kml: make sure your ciphers are working properly

    quit_ui = False
    while not quit_ui:
        # prompt 1: choose to encrypt or decrypt
        clear()
        print('Secret Messages!')
        print('=' * 16)
        [print(option) for option in main_menu]

        user_choice = input('> ')
        if user_choice == '1':
            cipher_method = 'encrypt'
        elif user_choice == '2':
            cipher_method = 'decrypt'
        elif user_choice.upper() == 'Q':
            break
        else:
            continue

        # prompt 2: choose which cipher to use
        while True:
            clear()
            print('Secret Messages!')
            print('=' * 16)
            print('Which cipher would you like to use for {}ion?:'.format(cipher_method))
            [print(option) for option in cipher_menu]

            # TODO-kml: is there a why to make this section more maintainable and DRY?
            cipher_choice = input('> ')
            if cipher_choice == '1':
                # use the Caesar Cypher
                print('Caesar Cipher')
                print('=' * 13)
                if cipher_method == 'encrypt':
                    message = input('Input a message to encrypt: ')
                    cipher = Caesar()
                    secret_message = cipher.encrypt(message)
                    print('Your secret message is: {}'.format(secret_message))
                    input('press any key to continue...')
                if cipher_method == 'decrypt':
                    secret_message = input('Input a message to decrypt: ')
                    cipher = Caesar()
                    message = cipher.decrypt(message)
                    print('Your decrypted message is: {}'.format(message))
                    input('press any key to continue...')
            elif cipher_choice == '2':
                # use the Alberti Cypher
                print('Alberti Cipher')
                print('=' * 13)
                if cipher_method == 'encrypt':
                    message = input('Input a message to encrypt: ')
                    cipher = Alberti()
                    secret_message = cipher.encrypt(message)
                    print('Your secret message is: {}'.format(secret_message))
                    input('press any key to continue...')
                if cipher_method == 'decrypt':
                    secret_message = input('Input a message to decrypt: ')
                    cipher = Alberti()
                    message = cipher.decrypt(message)
                    print('Your decrypted message is: {}'.format(message))
                    input('press any key to continue...')
            elif cipher_choice == '3':
                # use the Affine Cypher
                print('Affine Cipher')
                print('=' * 13)
                if cipher_method == 'encrypt':
                    message = input('Input a message to encrypt: ')
                    cipher = Affine()
                    secret_message = cipher.encrypt(message)
                    print('Your secret message is: {}'.format(secret_message))
                    input('press any key to continue...')
                if cipher_method == 'decrypt':
                    secret_message = input('Input a message to decrypt: ')
                    cipher = Affine()
                    message = cipher.decrypt(message)
                    print('Your decrypted message is: {}'.format(message))
                    input('press any key to continue...')
            elif cipher_choice == '4':
                # use the Atbash Cypher
                print('Atbash Cipher')
                print('=' * 13)
                if cipher_method == 'encrypt':
                    message = input('Input a message to encrypt: ')
                    cipher = Atbash()
                    secret_message = cipher.encrypt(message)
                    print('Your secret message is: {}'.format(secret_message))
                    input('press any key to continue...')
                if cipher_method == 'decrypt':
                    secret_message = input('Input a message to decrypt: ')
                    cipher = Atbash()
                    message = cipher.decrypt(message)
                    print('Your decrypted message is: {}'.format(message))
                    input('press any key to continue...')
            elif cipher_choice.upper() == 'B':
                break
            elif cipher_choice.upper() == 'Q':
                quit_ui = True
                break

    print('bye!')

if __name__ == '__main__':
    run_console_ui()
