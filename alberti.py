import random
import string


class Alberti:
    _CHAR_REPLACEMENTS = {'_': 'ZZ',
                          'H': 'FF',
                          'U': 'VV',
                          'Y': 'II',
                          'J': 'XX'}
    _PLAIN_TEXT_DISK = 'ABCDEFGIKLMNOPQRSTVWXZ1234'

    def __init__(self, key='A', cipher_disk='HDVEQYLRIJTCBPXWOSMZFNAKGU'):
        self.key = key.upper()
        self._CIPHER_DISK = cipher_disk

    def encrypt(self, text):
        # make sure there aren't any numbers in the text
        if any(char.isdigit() for char in text):
            raise ValueError("Please no numbers - write them out or use Roman numerals")

        # align the cipher disk key with the Plain Text disk letter A
        cipher = self._CIPHER_DISK
        cipher = cipher[cipher.index(self.key):] + cipher[:cipher.index(self.key)]

        # roll the dice, and insert numbers into

    # generates a random ordered alphabet to be used as a cipher disk
    def generate_cipher_disk(self):
        alphabet = list(string.ascii_uppercase)
        random.shuffle(alphabet)
        return ''.join(alphabet)



    # set a password for the Disk
    # needs an initial key P/b for example
    # there's an immovable disk A-Z + 1234
    # there's a movable inner disk which turns, and has a jumbled alphabet
    # adds rotational commands - roll 2 4-sided dice, determine # of chars & # to encode

    # ability to insert multiple numbers as a code book entry

    # need the same cipher disk...
    # but you also need the crib aka code book
    # CB or LC something that says - codebook, then 2 numbers
    # the code book entry redefines what the numbers mean

    #so, here's what we're gonna do
    def encrypt(self, message):
        pass

    def decrypt(self, message):
        pass