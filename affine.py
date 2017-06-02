import string


class Affine:
    def __init__(self):
        self.alphabet = string.ascii_uppercase

    def encrypt(self, text, a, b):
        """f(x) = (ax + b) mod alphabet_length"""
        # TODO-kml: validate variable a is co-prime w/ the length of the alphabet
        # TODO-kml: handle unsupported characters (e.g. numbers or punctuation)

        # transform the message into numbers
        coded_message = []
        for char in text.upper():
            try:
                num_val = self.alphabet.index(char)
            except ValueError:
                continue
            else:
                coded_message.append(num_val)

        # run the formula (ax + b) % alphabet_length & convert back to a letter
        for index in range(0, len(coded_message)):
            coded_message[index] *= a
            coded_message[index] += b
            coded_message[index] %= len(self.alphabet)
            new_letter = self.alphabet[coded_message[index]]
            coded_message[index] = new_letter
        return ''.join(coded_message)

    def decrypt(self, text, a, b):
        # transform the message into numbers
        coded_message = []
        for char in text.upper():
            try:
                num_val = self.alphabet.index(char)
            except ValueError:
                continue
            else:
                coded_message.append(num_val)

        # solve for a^-1
        # 1 = a * ? % m
        modular_inverse = 1
        while True:
            if a * modular_inverse % len(self.alphabet) == 1:
                break
            else:
                modular_inverse += 1

        # run the formula & convert back to a letter
        for index in range(0, len(coded_message)):
            coded_message[index] -= b
            coded_message[index] *= modular_inverse
            coded_message[index] %= len(self.alphabet)
            new_letter = self.alphabet[coded_message[index]]
            coded_message[index] = new_letter
        return ''.join(coded_message)
