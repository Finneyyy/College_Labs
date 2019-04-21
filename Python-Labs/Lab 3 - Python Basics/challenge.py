# Rot5, Rot13, and Rot47

rot13 = str.maketrans( "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
print(str.translate("What did you use to hash this", rot13))

# def rot47:

