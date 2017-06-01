from affine import Affine


class Atbash(Affine):
    """a special case of the Affine cipher..."""
    def __init__(self):
        super().__init__()
        self.affine_arg = len(self.alphabet) - 1

    def encrypt(self, text, a=None, b=None):
        return super().encrypt(text, self.affine_arg, self.affine_arg)

    def decrypt(self, text):
        return super().decrypt(text, self.affine_arg, self.affine_arg)

orig = Affine()
print(orig.encrypt('holy', 25, 25))
print(orig.decrypt('slob', 25, 25))

test = Atbash()
print(test.encrypt('abcdefghijklmnopqrstuvwxyz'))
print(test.decrypt('zyxwvutsrqponmlkjihgfedcba'))
