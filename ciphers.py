# TODO-kml: do some refactoring
# TODO-kml: add docstring descriptions
import random
import string


class Cipher:
    ALPHABET = string.ascii_uppercase

    def __init__(self):
        self.alphabet = Cipher.ALPHABET

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

# TODO-kml: maybe this can be the place to implement the OTP functionality
# TODO-kml: display encrypted output in 5 character blocks

    @classmethod
    def generate_ciphertext(cls):
        """generates a random ordered alphabet to be used as ciphertext"""
        alphabet = list(string.ascii_lowercase)
        random.shuffle(alphabet)
        return ''.join(alphabet)
