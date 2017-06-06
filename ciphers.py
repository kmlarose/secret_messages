import random
import string


class Cipher:
    """Parent class for all the different kinds of ciphers"""
    ALPHABET = string.ascii_uppercase

    def __init__(self):
        """Adds a standard English alphabet to each class instance"""
        self.alphabet = Cipher.ALPHABET

    def encrypt(self, text):
        """Returns encrypted text in 5 character blocks"""
        number_of_spaces = int(len(text) / 5)
        text_characters = list(text)
        for number in range(number_of_spaces):
            index = 5 * (number + 1)
            index += number
            text_characters.insert(index, ' ')
        return ''.join(text_characters)

    def decrypt(self, text):
        """Decrypts text by removing spaces"""
        text_characters = list(text)
        while ' ' in text_characters:
            text_characters.remove(' ')
        return ''.join(text_characters)
# TODO-kml: maybe this can be the place to implement the OTP functionality

    @staticmethod
    def generate_ciphertext():
        """generates a random ordered alphabet to be used as ciphertext"""
        alphabet = list(string.ascii_lowercase)
        random.shuffle(alphabet)
        return ''.join(alphabet)
