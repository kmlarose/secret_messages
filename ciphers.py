import random
import string


class Cipher:
    """Parent class for all the different kinds of ciphers"""
    ALPHABET = string.ascii_uppercase

    def __init__(self, otp_key='adrlagiurnlsidurabnlseiuban'):
        """Adds a standard English alphabet to each class instance"""
        self.alphabet = Cipher.ALPHABET
        self.otp_key = otp_key

    def encrypt(self, text):
        """Further encrypts the message with a unique One Time Pad and returns text in 5 character blocks."""
        code_message = []
        [code_message.append(self.alphabet.index(char.upper())) for char in text]
        code_otp = []
        [code_otp.append(self.alphabet.index(char.upper())) for char in self.otp_key]
        merged_code = [(code_message[index] + code_otp[index]) % 26 for index in range(len(code_message))]
        final_code = []
        [final_code.append(self.alphabet[number]) for number in merged_code]
        text = ''.join(final_code)

        # Returns encrypted text in 5 character blocks
        number_of_spaces = int(len(text) / 5)
        text_characters = list(text)
        for number in range(number_of_spaces):
            index = 5 * (number + 1)
            index += number
            text_characters.insert(index, ' ')
        return ''.join(text_characters)

    def decrypt(self, text):
        """Decrypts the One Time Pad. The result will also need to be decrypted by one of the cipher classes."""
        code_message = []
        [code_message.append(self.alphabet.index(char.upper())) for char in text]
        code_otp = []
        [code_otp.append(self.alphabet.index(char.upper())) for char in self.otp_key]
        decrypted_code = [(code_message[index] - code_otp[index]) % 26 for index in range(len(code_message))]
        ciphertext = []
        [ciphertext.append(self.alphabet[number]) for number in decrypted_code]
        text = ''.join(ciphertext)

        """Decrypts text by removing spaces"""
        text_characters = list(text)
        while ' ' in text_characters:
            text_characters.remove(' ')
        return ''.join(text_characters)

    @staticmethod
    def generate_ciphertext():
        """generates a random ordered alphabet to be used as ciphertext"""
        alphabet = list(string.ascii_lowercase)
        random.shuffle(alphabet)
        return ''.join(alphabet)
