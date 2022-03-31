from itertools import permutations
from math import pow
n = int(input())


number = pow(n,2)/2

numberstr= str(number)

array = []

for i in range(1,n+1):
    
    array.append(i)


permutation = permutations(array)

perm = list(permutation)

arraycheck = []

arraycheck1=[]

plus = 0

for i in perm:
    arraycheck.append(i)

    arraycheck1 = arraycheck[0]

    arraycheck.clear()

    for i in range(0,n-1):
        plus += abs(arraycheck1[i] -arraycheck1[i+1])
        

    if (plus>number):

        print("This permutaion is more than " + numberstr)

        print(arraycheck1)

        print(plus)

        plus = 0 

        

    else :

        print(" ")

        

