from ciphers import Cipher


class Caesar(Cipher):
    """Caesar Cipher shifts alphabet characters 3 places forward or backward"""
    FORWARD = Cipher.ALPHABET * 3

    def __init__(self, offset=3):
        super().__init__()
        self.offset = offset
        self.FORWARD = self.alphabet + self.alphabet[:self.offset+1]
        self.BACKWARD = self.alphabet[:self.offset+1] + self.alphabet

    def encrypt(self, text, one_time_pad):
        """Encrypt text by shifting alphabet characters 3 places forward"""
        # scrub spaces, numbers, and special chars from the input string
        text = list(text.upper())
        while any(char not in self.alphabet for char in text):
            for char in text:
                if char not in self.alphabet:
                    text.remove(char)
        text = ''.join(text)
        output = []
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return super().encrypt(''.join(output), one_time_pad)

    def decrypt(self, text, one_time_pad):
        """Decrypt text by shifting alphabet characters 3 places backward"""
        output = []
        text = super().decrypt(text, one_time_pad)
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)
