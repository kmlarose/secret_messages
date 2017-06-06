from ciphers import Cipher


class Caesar(Cipher):
    """Caesar Cipher shifts alphabet characters 3 places forward or backward"""
    FORWARD = Cipher.ALPHABET * 3

    def __init__(self, offset=3):
        super().__init__()
        self.offset = offset
        self.FORWARD = self.alphabet + self.alphabet[:self.offset+1]
        self.BACKWARD = self.alphabet[:self.offset+1] + self.alphabet

    def encrypt(self, text):
        """Encrypt text by shifting alphabet characters 3 places forward"""
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        """Decrypt text by shifting alphabet characters 3 places backward"""
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)
