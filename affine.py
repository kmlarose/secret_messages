from ciphers import Cipher


class Affine(Cipher):
    """Affine Cipher translates alphabet characters to numbers, transforms them with a mathematical formula,
    and then translates the numbers back into alphabet characters.
    This cipher accepts only alphabet characters and requires a pair of numbers as the key to translation"""
    def __init__(self, affine_key_a, affine_key_b):
        """Sets up the keys to encrypt and decrypt messages.
        The first key number cannot share any common factors with the alphabet length except for 1."""
        super().__init__()
        self.affine_key_a = affine_key_a
        if not Affine.is_valid_key_a(self.affine_key_a):
            raise ValueError("Key A cannot share any common factors with the alphabet length (except 1)")
        self.affine_key_b = affine_key_b

    def encrypt(self, text):
        """Encrypts text using this formula: f(x) = (ax + b) % m"""
        # transform the message into numbers
        coded_message = []
        for char in text.upper():
            try:
                num_val = self.alphabet.index(char)
            except ValueError:
                continue
            else:
                coded_message.append(num_val)

        # run the formula (ax + b) % m and convert back to a letter
        for index in range(0, len(coded_message)):
            coded_message[index] *= self.affine_key_a
            coded_message[index] += self.affine_key_b
            coded_message[index] %= len(self.alphabet)
            new_letter = self.alphabet[coded_message[index]]
            coded_message[index] = new_letter
        return super().encrypt(''.join(coded_message))

    def decrypt(self, text):
        """Decrypts text using this formula: a^-1 (x - b) % m"""
        text = super().decrypt(text)
        # transform the message into numbers
        coded_message = []
        for char in text.upper():
            try:
                num_val = self.alphabet.index(char)
            except ValueError:
                continue
            else:
                coded_message.append(num_val)

        # solve for a^-1 by using this formula: 1 = a * (a^-1) % m
        modular_multiplicative_inverse = 1
        while True:
            if self.affine_key_a * modular_multiplicative_inverse % len(self.alphabet) == 1:
                break
            else:
                modular_multiplicative_inverse += 1

        # run the formula a^-1 (x - b) % m and convert back to a letter
        for index in range(0, len(coded_message)):
            coded_message[index] -= self.affine_key_b
            coded_message[index] *= modular_multiplicative_inverse
            coded_message[index] %= len(self.alphabet)
            new_letter = self.alphabet[coded_message[index]]
            coded_message[index] = new_letter
        return ''.join(coded_message)

    @staticmethod
    def is_valid_key_a(key):
        """Determine if the key is co-prime with the length of the alphabet.
        That is, if the only positive integer that divides both of them is 1"""
        alphabet_factors = set()
        alphabet_length = len(Affine.ALPHABET)
        possible_factors = list(range(alphabet_length+1))[1:]
        for number in possible_factors:
            if alphabet_length % number == 0:
                alphabet_factors.add(number)

        key_factors = set()
        possible_factors = list(range(key+1))[1:]
        for number in possible_factors:
            if key % number == 0:
                key_factors.add(number)

        shared_factors = list(alphabet_factors & key_factors)
        return len(shared_factors) == 1
