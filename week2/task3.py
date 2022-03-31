from itertools import permutations



n = int(input())

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

      plus +=  arraycheck1[n-1-i]-arraycheck1[n-1-(i+1)]
      


    
    if (plus>0):

        print("This permutaion in acending order")

        print(arraycheck1)

        

    else :

        print(" ")
