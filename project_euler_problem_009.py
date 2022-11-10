'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
def find_pythagorean(n):
    '''
    Returns a Pythagorean triplet a, b, c where a + b + c = n
    '''
    for a in range(1, int(n/2)):
        for b in range(1, int(n/2)):
            if a**2+b**2==(n-a-b)**2:
                return [a, b, n-a-b]
    return 'not found!'

n = 10000
x = find_pythagorean(n)
print('a =', x[0], ', b =', x[1], ', c =', x[2])
print('abc =', x[0]*x[1]*x[2])

