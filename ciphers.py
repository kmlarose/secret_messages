import random
import string


class Cipher:
    """Parent class for all the different kinds of ciphers"""
    ALPHABET = string.ascii_uppercase

    def __init__(self):
        """Adds a standard English alphabet to each class instance"""
        self.alphabet = Cipher.ALPHABET

    def encrypt(self, text):
        """Encrypts text"""
        raise NotImplementedError()

    def decrypt(self, text):
        """Decrypts text"""
        raise NotImplementedError()

# TODO-kml: maybe this can be the place to implement the OTP functionality
# TODO-kml: display encrypted output in 5 character blocks

    @staticmethod
    def generate_ciphertext():
        """generates a random ordered alphabet to be used as ciphertext"""
        alphabet = list(string.ascii_lowercase)
        random.shuffle(alphabet)
        return ''.join(alphabet)
