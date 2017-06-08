from ciphers import Cipher
import random


class Alberti(Cipher):
    """Alberti Cipher models an ancient device with two rotating disks.
    This class encrypts and decrypts text using a unique string of ciphertext (random alphabet characters).
    The mapping of ciphertext to plain text letters randomly shifts every 1-4 characters"""
    def __init__(self, key='A', cipher_disk='hdveqylrijtcbpxwosmzfnakgu'):
        super().__init__()
        self._PLAIN_TEXT_DISK = 'ABCDEFGIKLMNOPQRSTVWXZ1234'
        # validate the ciphertext str is the same length as the plain text str
        if len(cipher_disk) != len(self.alphabet):
            raise ValueError('ciphertext string must be equal length to plaintext string: {} chars'.format(len(self._PLAIN_TEXT_DISK)))
        self.key = key
        self._CIPHER_DISK = cipher_disk.lower()
        self._CHAR_REPLACEMENTS = {' ': 'ZZ',
                                   'H': 'FF',
                                   'U': 'VV',
                                   'Y': 'II',
                                   'J': 'XX'}

    def encrypt(self, text, one_time_pad):
        """Encrypts text by mapping letters to the cipher text.
        Randomly shifts key to ciphertext every 1-4 characters."""
        # make sure there aren't any numbers in the text
        if any(char.isdigit() for char in text):
            raise ValueError("Please no numbers - write them out or use Roman numerals")
        coded_message = text.upper()
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
                cipher = Alberti.rotate_cipher(self._CIPHER_DISK, self.key)

        coded_message = ''.join(coded_message)
        return super().encrypt(coded_message.upper())

    def decrypt(self, text, one_time_pad):
        """Decrypts text using the Alberti method"""
        text = super().decrypt(text)
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
                cipher = Alberti.rotate_cipher(self._CIPHER_DISK, self.key)

        # remove the numbers from the message
        remove_list = []
        for char in message:
            if char.isdigit():
                remove_list.append(char)
        [message.remove(char) for char in remove_list]

        # swap out character replacements
        message = ''.join(message)
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
        """Reset the ciphertext to the original alignment"""
        return Alberti.rotate_cipher(self._CIPHER_DISK, self.key)

    @staticmethod
    def rotate_cipher(cipher_disk, first_letter):
        """Rearranges the ciphertext string to begin with the key"""
        cipher_disk = cipher_disk.lower()
        first_letter = first_letter.lower()
        shift = cipher_disk.index(first_letter)
        return cipher_disk[shift:] + cipher_disk[:shift]
