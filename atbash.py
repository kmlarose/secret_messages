from affine import Affine


class Atbash(Affine):
    """Atbash is a special case of the Affine cipher.
    It maps an alphabet to itself in reverse"""
    def __init__(self):
        """Atbash is an Affine cipher with both key values set to the alphabet length - 1"""
        self.affine_arg = len(Affine.ALPHABET) - 1
        super().__init__(self.affine_arg, self.affine_arg)

    def encrypt(self, text):
        """Encrypts text using the Atbash cipher method"""
        return super().encrypt(text)

    def decrypt(self, text):
        """Decrypts text using the Atbash cipher method"""
        return super().decrypt(text)
