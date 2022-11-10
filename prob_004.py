'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome():
    iter = 0
    palindrome_max = 0

    for i in range(999, round((100+999)/2)+1, -1):
        for j in range(999, 99, -1):
            if is_palindrome(i*j):
                palindrome_max = max(i*j, palindrome_max)

    return palindrome_max

print(largest_palindrome())