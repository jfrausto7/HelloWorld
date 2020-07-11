import math

"""This is a primality test based on Trial Division. It's runtime is O(N)."""

def isPrimeTD(n):
    i = 2
    k = math.sqrt(n)

    #iterate through now
    while(i <= k):
        #if the numbers under k is a factor of n, return false
        if n % i == 0:
            return False

    return True