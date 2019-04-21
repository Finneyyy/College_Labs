#! usr/bin/venv python
import hashlib

loop=5000
while loop==5000:
    first_string="Hello World!"
    print(first_string)
    print(hashlib.md5(first_string.encode()).hexdigest())


