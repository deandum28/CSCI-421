from string import ascii_uppercase
from itertools import product
from re import findall
 
def uniq(seq):
    seen = {}
    return [seen.setdefault(z, z) for z in seq if z not in seen]
 
def division(seq, n):
    return [seq[i : i + n] for i in xrange(0, len(seq), n)]
 
 
def playfair(key, from_ = 'J', to = None):
    if to is None:
        to = 'I' if from_ == 'J' else ''
 
    def refine(s):
        return filter(str.isupper, s.upper()).replace(from_, to)
        
    matrix = division(uniq(refine(key + ascii_uppercase)), 5)
     	
    encrypt = {}
 
    for row in matrix:
        for i, j in product(xrange(5), repeat=2):
            if i != j:
                encrypt[row[i] + row[j]] = row[(i + 1) % 5] + row[(j + 1) % 5]
 
    for c in zip(*matrix):
        for i, j in product(xrange(5), repeat=2):
            if i != j:
                encrypt[c[i] + c[j]] = c[(i + 1) % 5] + c[(j + 1) % 5]
 
    for i1, j1, i2, j2 in product(xrange(5), repeat=4):
        if i1 != i2 and j1 != j2:
            encrypt[matrix[i1][j1] + matrix[i2][j2]] = matrix[i1][j2] + matrix[i2][j1]
 
    decrypt = dict((v, k) for k, v in encrypt.iteritems())
 
    def enc2(txt):
        exclusionList = findall(r"(.)(?:(?!\1)(.))?", refine(txt))
        return " ".join(encrypt[a + (b if b else 'X')] for a, b in exclusionList)
 
    def dec2(encoded):
        return " ".join(decrypt[p] for p in division(refine(encoded), 2))
 
    return enc2, dec2

