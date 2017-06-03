from affine import Affine


# TODO-kml: do some refactoring
# TODO-kml: add docstring descriptions
class Atbash(Affine):
    """a special case of the Affine cipher..."""
    def __init__(self):
        self.affine_arg = len(Affine.ALPHABET) - 1
        super().__init__(self.affine_arg, self.affine_arg)

    def encrypt(self, text):
        return super().encrypt(text)

    def decrypt(self, text):
        return super().decrypt(text)
