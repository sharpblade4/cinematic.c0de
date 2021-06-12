"""
Mr. Robot - s3e10 52:43

Also appears in scene:
  - https://github.com/livz/cloacked-pixel
  - https://domnit.org/stepic/doc/
  
"""


from Crypto.Protocol.KDF import PBKDF2
from Crypto.PublicKey import RSA
import getpass

infile = raw_input(“File: “)
f = open(infile, ‘r’)
password = getpass.getpass()
f.seek(1024)
salt = f.read(32)

master = PBKDF2(password, salt, count=10000)

def notrand(n):
    notrand.i += 1
    return PBKDF2(master, str(notrand.i), dkLen=n, count=1)

notrand.i = 0
RSA_key = RSA.generate(4096, randfunc=notrand)
print RSA_key.exportKey()
