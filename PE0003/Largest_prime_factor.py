"""
Project Euler
Problem 3
Largest prime factor
Aaron Mok
08/09/14
"""
import math
#Overflow error, method doesn't work
def largest_prime(num):
    arr = [True] * num
    root = math.sqrt(num)
    root = math.ceil(root)
    for i in range(2,root,1):
        if arr[i] is True:
            for j in range(i*i, num, i):
                arr[j] = False
    for i in range(len(arr)):
        if arr[i] == True:
            print(i)


largest_prime(600851475143)