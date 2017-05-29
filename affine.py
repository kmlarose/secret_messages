import string


class Affine:
    def __init__(self):
        self.alphabet = string.ascii_uppercase

    def encrypt(self, text, a, b):
        """f(x) = (ax + b) mod alphabet_length"""
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


# lil' test to help me out while I'm developing the class
if __name__ == '__main__':
    text_cipher = Affine()
    secret_message = text_cipher.encrypt('affinecipher', 5, 8)
    print(secret_message)
