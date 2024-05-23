"""
We use r+b mode is used for reading and writing mode b is for binary mode
r+b mode is open the binary file in read or write mode
"""

with open("heart.gif", "r+b")as f:
    data = f.read(1)
    if data == b'G':
        f.seek(0)
        f.write(b'S')
    elif data == b'S':
        f.seek(0)
        f.write(b'G')

