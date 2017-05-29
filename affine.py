import string


class Affine:
    def __init__(self):
        self.alphabet = string.ascii_uppercase
        self.numbers = list(range(0, 26))

    def encrypt(self, text):
        # transform the message into numbers
        coded_message = []
        for char in text:
            num_val = text.index()

        # chr(x) for x = 65 - 90 is the capital letters
