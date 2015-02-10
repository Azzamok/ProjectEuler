"""
Project Euler
Problem 2
Even Fibonacci numbers
Aaron Mok
21/05/14
"""
import time


def fib(num):
    fiblist = [1, 2] #Base case
    count = 0 #Initial value counter
    while count <= num: #Counting until it is no greater than num (4,000,000)
        count = fiblist[-1] + fiblist[-2] #Generating next fibonacci number
        fiblist.append(count)
    ans = 0
    for i in range(len(fiblist)):
        if fiblist[i] % 2 == 0: #Getting all even Fibonacci numbers
            ans += fiblist[i]
    print(ans)


def main():
    start = time.clock()
    fib(4000000)
    taken = round((time.clock() - start), 4)
    print("Time to complete algorithm is:", taken, "seconds.")


if __name__ == '__main__':
    main()




#Optimal solution
"""
F(n)=4*F(n-3)+F(n-6)
"""

#Further insights
"""
- If we only write the even numbers:
    2 8 34 144...
    it seems that they obey the following recursive relation: E(n)=4*E(n-1)+E(n-2)
"""