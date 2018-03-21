import hashlib
import struct

def NByte(VALUE, n):
    h = hex((VALUE&(0xFF<<(8*n)))>>(8*n))
    if len(h) > 1 and h[0:2] == '0x':
        h = h[2:]
    if len(h) % 2:
        h = "0" + h
    return h

for i in range(0, 16581375):
    x = NByte(i,0)
    z = NByte(i,1)
    y = NByte(i,2)
    t = struct.pack('<L', i)[:3]
    md5hash = hashlib.md5(t).hexdigest()
    if (x+z+y) == md5hash[:6]:
        print "Found one! " + str(i)
        print "Hash: " + md5hash