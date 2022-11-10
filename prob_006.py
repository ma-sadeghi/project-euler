'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
n = 10000000

# optimized version
sum_of_squared = n*(n+1)*(2*n+1)//6
sum_squared = (n*(n+1)//2)**2

print(sum_squared - sum_of_squared)

# lame version
sum_of_squared = sum([x**2 for x in range(1, n+1)])
sum_squared = sum(range(1, n+1))**2

print(sum_squared - sum_of_squared)