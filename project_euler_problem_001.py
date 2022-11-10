'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below n = 1000.
'''
n = 1000

# optimized implementation
def sum_divisable_by(p, m):
    n = p // m
    a1 = m
    an = p - p % m
    sn = (a1 + an) * n / 2
    
    return sn
    
print(int(
    + sum_divisable_by(n-1,3)
    + sum_divisable_by(n-1,5)
    - sum_divisable_by(n-1,15)))   