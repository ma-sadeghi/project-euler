'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from utils import *

n = 2000000

def sum_primes_below(n):
    '''
    Returns the sum of all primes below n.
    '''
    s = 2
    for i in range(3, n, 2):
        if is_prime(i):
            s += i
    return s

print(sum_primes_below(n))
