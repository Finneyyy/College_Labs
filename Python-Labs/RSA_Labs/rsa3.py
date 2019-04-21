# help gotten from https://stackoverflow.com/questions/42504079/how-do-you-extract-n-and-e-from-a-rsa-public-key-in-python
from Crypto.PublicKey import RSA

pub_key = RSA.importKey(open('mykey2', 'r').read())

print(pub_key.n)
print()
print(pub_key.e)
print(pub_key.d)

