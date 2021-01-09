import time
import sys

sys.setrecursionlimit(10000)

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

def factorial2(n):
    total = 1
    long(total)
    for i in range(1,n+1):
        total *= i
    return total

start = time.time()

number = 5000

print(factorial(number), "\n", time.time()-start, "\n", 40*"=")
updated = time.time()

print(factorial2(number), "\n", time.time()-updated)