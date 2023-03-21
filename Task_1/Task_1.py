"""
Task 1. What is FOR loop?
"""
N = int(input('Enter positive integer number N: '))
result = 0

for i in range(1, N + 1):
    result += i
""" 
Or the same thing, just without for loop:
result = sum(range(1, N + 1))
"""

print(result)