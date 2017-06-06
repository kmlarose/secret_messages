from affine import Affine
from alberti import Alberti
from atbash import Atbash
from caesar import Caesar
import os

# TODO-kml: test your program - how does it handle spaces, special chars, empty str inputs? Can you throw Exceptions?


def clear():
    """Clears text off the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_underlined(text):
    """Prints the text underlined with ='s"""
    print(text)
    print('=' * len(text))


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
        '1: Affine Cipher',
        '2: Alberti Cipher',
        '3: Atbash Cipher',
        '4: Caesar Cipher',
        'H: Help',
        'B: Back to Main Menu',
        'Q: Quit']

    quit_ui = False
    while not quit_ui:
        # prompt 1: choose to encrypt or decrypt
        clear()
        print_underlined('Secret Messages!')
        print('Choose to encrypt or decrypt a message:')
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
            print_underlined('Secret Messages! {} MODE'.format(cipher_method.upper()))
            print('Which cipher would you like to use for {}ion?:'.format(cipher_method))
            [print(option) for option in cipher_menu]
            cipher_choice = input('> ')
            if cipher_choice == '1':
                clear()
                print_underlined('Affine Cipher | {} Mode'.format(cipher_method.title()))
                print("Please provide two numbers as the key for the Affine Cipher")
                # get the keys, loop through input until a valid number is provided
                affine_key_a = ''
                while not isinstance(affine_key_a, int):
                    affine_key_a = input('Enter the first key number: ')
                    try:
                        affine_key_a = int(affine_key_a)
                    except ValueError:
                        print('please provide an integer...')
                    else:
                        if not Affine.is_valid_key_a(affine_key_a):
                            print('The first key cannot share any common factors (other than 1)')
                            print('with the length of the alphabet: {}'.format(len(Affine.ALPHABET)))
                            print('hint: try an odd number (but, not 13)')
                            input('enter to try again.')
                            affine_key_a = ''

                affine_key_b = ''
                while not isinstance(affine_key_b, int):
                    affine_key_b = input('Enter the second key number: ')
                    try:
                        affine_key_b = int(affine_key_b)
                    except ValueError:
                        print('please provide an integer...')

                cipher = Affine(affine_key_a, affine_key_b)
            elif cipher_choice == '2':
                outer_ring = 'ABCDEFGIKLMNOPQRSTVWXZ1234'
                inner_ring = 'hdveqylrijtcbpxwosmzfnakgu'
                while True:
                    clear()
                    print_underlined('Alberti Cipher | {} Mode'.format(cipher_method.title()))
                    print('This cipher models an ancient device that aligns two disks:')
                    print('an outer disk with Plain Text, and an inner disk with Ciphertext')
                    print('Enter the inner ring character to align with outer ring A:')
                    print('Outer Ring: {}'.format(outer_ring))
                    print('Inner Ring: {}'.format(inner_ring))

                    key = input('> ')
                    key = key.lower()
                    if key in inner_ring:
                        inner_ring = Alberti.rotate_cipher(inner_ring, key)
                        clear()
                        print_underlined('Alberti Cipher')
                        print('This cipher models an ancient device that aligns two disks:')
                        print('an outer disk with Plain Text, and an inner disk with Ciphertext')
                        print('Enter the inner ring character to align with outer ring A:')
                        print('Outer Ring: {}'.format(outer_ring))
                        print('Inner Ring: {}'.format(inner_ring))
                        if input('Is this right [Y/n]?').lower() != 'n':
                            break
                cipher = Alberti(key=key, cipher_disk=inner_ring)
            elif cipher_choice == '3':
                clear()
                print_underlined('Atbash Cipher | {} Mode'.format(cipher_method.title()))
                cipher = Atbash()
            elif cipher_choice == '4':
                clear()
                print_underlined('Caesar Cipher | {} Mode'.format(cipher_method.title()))
                cipher = Caesar()
            elif cipher_choice.upper() == 'H':
                # TODO-kml: explain what these ciphers do - maybe use the class docstrings?
                print("Help coming soon... in the meantime, please search the web")
                input('press any key to continue...')
                continue
            elif cipher_choice.upper() == 'B':
                break
            elif cipher_choice.upper() == 'Q':
                quit_ui = True
                break
            else:
                continue

            # get the user's message and translate it using the chosen cipher & method
            users_message = input('Input a message to {}: '.format(cipher_method))
            translation = getattr(cipher, cipher_method)(users_message)
            print('Translation: {}'.format(translation))
            input('press enter to continue...')
    print('bye!')

if __name__ == '__main__':
    run_console_ui()
