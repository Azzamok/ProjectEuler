"""
Project Euler
Problem 1
Multiples of 3 and 5
Aaron Mok
21/05/14
"""
import time


def mult():
    num = input("Enter a number: ")
    start = time.clock()
    ans = 0
    for i in range(int(num)):
        if i % 3 == 0: #Multiple of 3
            ans += i
        elif i % 5 == 0: #Multiple of 5
            ans += i
    print(ans)
    taken = round((time.clock() - start), 4)
    print("Time to complete algorithm is:", taken, "seconds.")
    
def main():
    mult()



if __name__ == '__main__':
    main()





#Optimal solution
"""
print(sum([x for x in xrange(3,1000) if (not x % 3) or (not x % 5)])
"""

#Further insights
"""
- num/multiples -> add them -> subtract any conflicting multiples => ans
- sumdivby(3) + sumdivby(5) - sumdiv(15) = ans
"""