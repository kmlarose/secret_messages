from ciphers import Cipher
import random
import string


# TODO-kml: do some refactoring
# TODO-kml: add docstring descriptions
class Alberti(Cipher):
    """
    Alberti Cipher models an ancient device with two rotating disks.
    This class encrypts and decrypts text using a unique string of ciphertext (random alphabet characters).
    The mapping of ciphertext to plain text letters randomly shifts every 1-4 characters
    """
    def __init__(self, cipher_disk='hdveqylrijtcbpxwosmzfnakgu'):
        # TODO-kml confirm that the cipher_disk has 26 chars - or more appropriately, it matches len(alphabet)
        self._CIPHER_DISK = cipher_disk.lower()
        self._CHAR_REPLACEMENTS = {' ': 'ZZ',
                                   'H': 'FF',
                                   'U': 'VV',
                                   'Y': 'II',
                                   'J': 'XX'}
        self._PLAIN_TEXT_DISK = 'ABCDEFGIKLMNOPQRSTVWXZ1234'

    def encrypt(self, text):
        # make sure there aren't any numbers in the text
        if any(char.isdigit() for char in text):
            raise ValueError("Please no numbers - write them out or use Roman numerals")
        coded_message = text.upper()

        # align the cipher disk key with the Plain Text Disk letter A
        cipher = self.reset_cipher()

        # replace any characters in the text which do not appear on the plain text disk
        for char, replacement in self._CHAR_REPLACEMENTS.items():
            coded_message = coded_message.replace(char, replacement)

        # randomly add numbers to the message to represent cipher disk rotations
        index = 0
        coded_message = list(coded_message)
        while index < len(coded_message):
            # determine where to add the cipher shift
            index += random.randint(1, 4)

            # determine how many rotations to shift the cipher
            cipher_shift = str(random.randint(1, 4))

            # insert the number into the coded message
            coded_message.insert(index, cipher_shift)
            index += 1

        # replace the characters of the message with the cipher characters
        for char in coded_message:
            # find the character on the Plain Text Disk
            disk_index = self._PLAIN_TEXT_DISK.index(char)
            # record the cipher disk character at this location
            coded_message[coded_message.index(char)] = cipher[disk_index]

            # if the character is a number, then rotate the cipher code
            if char.isdigit():
                cipher = self.rotate_cipher(cipher, int(char))

        coded_message = ''.join(coded_message)
        return coded_message.upper()

    def decrypt(self, text):
        # align the cipher disk key with the Plain Text Disk letter A
        cipher = self.reset_cipher()

        # decrypt the characters in the coded message
        message = list(text.lower())
        for char in message:
            # find the character on the Cipher Disk
            disk_index = cipher.index(char)
            # record the Plain Text Disk character at this location
            message[message.index(char)] = self._PLAIN_TEXT_DISK[disk_index]

            # if the character is a number, then rotate the cipher code backwards
            new_char = message[message.index(self._PLAIN_TEXT_DISK[disk_index])]
            if new_char.isdigit():
                shift = int(new_char)
                cipher = self.rotate_cipher(cipher, shift)

        # remove the numbers from the message
        remove_list = []
        for char in message:
            if char.isdigit():
                remove_list.append(char)
        for char in remove_list:
            message.remove(char)

        # swap out character replacements
        message = ''.join(message)
        # import pdb; pdb.set_trace()
        for char, replacement in self._CHAR_REPLACEMENTS.items():
            # identify if there are any occurrences of the special characters
            try:
                message.index(replacement)
            except ValueError:
                continue
            else:
                message = message.replace(replacement, char)
        return message

    def reset_cipher(self):
        return self.rotate_cipher(self._CIPHER_DISK, self._CIPHER_DISK.index('a'))

    @classmethod
    def rotate_cipher(cls, cipher, shift):
        return cipher[shift:] + cipher[:shift]
