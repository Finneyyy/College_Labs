import hashlib
ecsc="c89aa2ffb9edcc6604005196b5f0e0e4"
hash1=hashlib.md5()

def HashIt():
    some_string= "Hello World!"
    hash1=hashlib.md5()
    hash1.update(some_string.encode('utf-8'))
    hash1.update(hash1.encode())
    print(hash1.hexdigest())
    while(hash1 != ecsc):
        HashIt()
    else:
        print(hash1.hexdigest())
print(hash1.hexdigest())
