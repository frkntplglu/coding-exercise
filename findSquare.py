import math

def isPerfectSquare(n):
    sqr = math.sqrt(n)
    if(sqr - math.floor(sqr) == 0):
        return 1
    return 0

def nextPerfectSquare(n):
    if(isPerfectSquare(n)):
        nextP = math.isqrt(n) + 1
        return nextP * nextP
    return -1
  


print(nextPerfectSquare(225))