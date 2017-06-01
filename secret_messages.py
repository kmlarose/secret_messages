from affine import Affine
from alberti import Alberti
from caesar import Caesar
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def run_console_ui():
    main_menu = [
        '1: Caesar Cipher',
        '2: Alberti Cipher',
        '3: Affine Cipher',
        '4: Atbash Cipher',
        '0: Quit'
    ]
    while True:
        clear()
        print('Secret Messages!')
        print('=' * 16)
        print('Which cipher would you like to use?:')
        for option in main_menu:
            print(option)

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
            secret_message = text_cipher.encrypt('affinecipher', 25, 25)
            print(secret_message)
            original_message = text_cipher.decrypt('ZUURMVXRKSVI', 25, 25)
            print(original_message)
            input('press any key to continue...')
        elif cipher_choice == '4':
            print('Atbash test')
            test = Affine()
            print(test.encrypt('rip', 25, 25))
            input('press any key to continue...')
        elif cipher_choice == '0':
            print('bye!')
            break


if __name__ == '__main__':
    run_console_ui()
