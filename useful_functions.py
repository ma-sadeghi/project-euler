'''
Some useful functions to use for solving Project Euler's problems
'''

def is_prime(n):
    '''
    Returns true if n is a prime number.
    '''
    if type(n) != int:
        print(n, 'is not integer; will use', int(n), 'instead')

    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False

    return True

def nth_prime(n):
    '''
    Returns the n'th prime number.
    '''

    # lame implementation
    '''
    prime_counter = 0
    p = 2
    while prime_counter != n:
        if is_prime(p):
            prime_counter += 1
        p += 1

    return p-1
    '''

    # optimized implementation
    if n == 1:
        return 2
    elif n == 2:
        return 3

    prime_counter = 2
    k = 1

    while prime_counter < n:
        if is_prime(6*k-1):
            prime_counter += 1
            p = 6*k-1
        if is_prime(6*k+1):
            prime_counter += 1
            p = 6*k+1
        k += 1

    return (p - (prime_counter==n+1)*2)

def string_product(s):
    from functools import reduce
    from operator import mul

    '''
    Returns the product of all digits inside a string containing digits only.
    '''
    if str.isdigit(s) != True:
        print('warning:', s, 'contains non-digit characters')
        return 0
    return reduce(mul, list(map(int, list(s))), 1)