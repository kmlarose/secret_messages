from alberti import Alberti
from caesar import Caesar


secret_message = 'how does this look encrypted?'

# test the Caesar Cypher
print('Caesar Test')
print('='*11)
julius = Caesar()
print(julius.encrypt('abc'))
print(julius.decrypt('def'))

# test the Alberti Cypher
print('\nAlberti Test')
print('='*12)
cipher = Alberti()
print(cipher.encrypt('what happens here'))
print(cipher.decrypt('WDDAZWZZKRRUQSHMJONVVVBQXYXULWR'))