from math import log2
from math import floor
from time import time

start = time()

def josephus(n): 
    return 2*(n-(2**floor(log2(n))))


pattern = []
for a in range(1, 4000000, 1):
    pattern.append((josephus(a), a))

print(pattern)
print(time()-start)

"""
a = floor(log2(n)) #varv

overflow = n-2**a #över närmsta tvåpotens

tal = 2*overflow #antal 2:or över 0

maxtal = 2*((2**a)-1)
print(overflow, maxtal, a, tal)
"""
