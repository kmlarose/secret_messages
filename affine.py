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
        """d(x) = mod_inverse(a) * (y - b)"""
        # transform the message into numbers
        coded_message = []
        for char in text.upper():
            try:
                num_val = self.alphabet.index(char)
            except ValueError:
                continue
            else:
                coded_message.append(num_val)

        # run the formula & convert back to a letter
        modular_inverse = len(self.alphabet) - (a % len(self.alphabet))
        for index in range(0, len(coded_message)):
            coded_message[index] -= b
            coded_message[index] *= modular_inverse
            coded_message[index] %= len(self.alphabet)
            new_letter = self.alphabet[coded_message[index]]
            coded_message[index] = new_letter
        return ''.join(coded_message)

# lil' test to help me out while I'm developing the class
if __name__ == '__main__':
    text_cipher = Affine()
    secret_message = text_cipher.encrypt('affinecipher', 5, 8)
    print(secret_message)
    original_message = text_cipher.decrypt('IHHWVCSWFRCP', 5, 8)
    print(original_message)