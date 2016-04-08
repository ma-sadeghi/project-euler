'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
from operator import mul
from functools import reduce

def factor(n):
    lst = []
    for i in range(2, n):
        while True:
            if n % i == 0:
                lst.append(i)
                n /= i
            else:
                break

    if lst == []:
        return [n]
    else:
        return lst

def least_common_multiple(n):
    ans = []
    for i in range(2, n+1):
        m1 = factor(i)
        s1 = set(m1)
        s2 = set(ans)
        for element in s1:
            if element in s2:
                if ans.count(element) < m1.count(element):
                    [ans.append(element) for j in range(m1.count(element)-ans.count(element))]
            else:
                [ans.append(element) for j in range(m1.count(element))]

    return reduce(mul, ans, 1)

print(least_common_multiple(30))