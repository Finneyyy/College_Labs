from Crypto.PublicKey import RSA

priv_key = RSA.importKey(open('mykey3', 'r').read())
