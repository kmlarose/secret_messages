from caesar import Caesar


secret_message = 'how does this look encrypted?'
backwards_message = '?detpyrcne kool siht seod woh'

# three ciphers are used to encrypt and decrypt


# backwards encryption!
def encrypt(message):
    coded_message = []
    for letter in list(message)[::-1]:
        coded_message.append(letter)
    return ''.join(coded_message)


def decrypt(coded_message):
    message = []
    for letter in list(coded_message)[::-1]:
        message.append(letter)
    return ''.join(message)

print(encrypt(secret_message))
print(decrypt(backwards_message))

# create the Caesar Cypher
julius = Caesar()
print(julius.encrypt('abc'))
print(julius.decrypt('def'))

