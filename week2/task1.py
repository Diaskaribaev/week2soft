from itertools import permutations
from math import factorial,sqrt
n = int(input())


number = sqrt(factorial(n))

numberstr= str(number)

array = []

for i in range(1,n+1):

    array.append(i)


permutation = permutations(array)

perm = list(permutation)

arraycheck = []

arraycheck1=[]

multiplication = 1

for i in perm:
    arraycheck.append(i)

    arraycheck1 = arraycheck[0]

    arraycheck.clear()

    for i in range(0,n-1):
        multiplication *= abs(arraycheck1[i] -arraycheck1[i+1])

    if (multiplication<number):

        print("This permutaion is less than " + numberstr)

        print(arraycheck1)
        
        multiplication = 1

        

    else :

        print(" ")

        

