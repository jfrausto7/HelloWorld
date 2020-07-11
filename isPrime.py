import math

"""This is another primality test, but this is based off of the fact that any prime
number can be represented by 6k +- 1, where k is an integer. It's runtime is O(sqrt(n))"""
def isPrime(n):
    #first get the corner cases
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        #this is the main meat of the function, where we iterate through possible factors up to n
        i = 5
        while i * i <= n:
            if n % i == 0  or n % i + 2 == 0:
                return False
            i += 6  #increment by 6 because of 6k+1

        #else return true
        return True