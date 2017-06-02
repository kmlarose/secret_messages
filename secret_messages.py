from affine import Affine
from alberti import Alberti
from atbash import Atbash
from caesar import Caesar
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def run_console_ui():
    main_menu = [
        '1: Encrypt a Message',
        '2: Decrypt a Message',
        'Q: Quit'
    ]
    cipher_menu = [
        '1: Caesar Cipher',
        '2: Alberti Cipher',
        '3: Affine Cipher',
        '4: Atbash Cipher',
        'B: Back to Main Menu',
        'Q: Quit'
    ]
    while True:
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
        clear()
        print('Which cipher would you like to use?:')
        [print(option) for option in cipher_method]

        cipher_choice = input('> ')
        if cipher_choice == '1':
            # test the Caesar Cypher
            print('Caesar Test')
            print('=' * 11)
            julius = Caesar()
            print(julius.encrypt('abc'))
            print(julius.decrypt('def'))
            input('press any key to continue...')
        elif cipher_choice == '2':
            # test the Alberti Cypher
            print('\nAlberti Test')
            print('=' * 12)
            alb_ciph = Alberti()
            print(alb_ciph.encrypt('what happens here'))
            print(alb_ciph.decrypt('WDDAZWZZKRRUQSHMJONVVVBQXYXULWR'))
            input('press any key to continue...')
        elif cipher_choice == '3':
            affine = Affine()
            print('Affine test... {} work in progress'.format(affine))
            text_cipher = Affine()
            secret_message = text_cipher.encrypt('affinecipher', 5, 8)
            print(secret_message)
            original_message = text_cipher.decrypt('ZUURMVXRKSVI', 5, 8)
            print(original_message)
            input('press any key to continue...')
        elif cipher_choice == '4':
            print('Atbash test')
            test = Atbash()
            print(test.encrypt('holy'))
            print(test.decrypt('slob'))
            input('press any key to continue...')
        elif cipher_choice.upper() == 'B':
            continue
        elif cipher_choice.upper() == 'Q':
            break

    print('bye!')

if __name__ == '__main__':
    run_console_ui()
