from affine import Affine


# TODO-kml: do some refactoring
# TODO-kml: add docstring descriptions
class Atbash(Affine):
    """a special case of the Affine cipher..."""
    def __init__(self):
        super().__init__()
        self.affine_arg = len(self.alphabet) - 1

    def encrypt(self, text, a=None, b=None):
        return super().encrypt(text, self.affine_arg, self.affine_arg)

    def decrypt(self, text):
        return super().decrypt(text, self.affine_arg, self.affine_arg)
