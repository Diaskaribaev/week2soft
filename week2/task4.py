from itertools import permutations



n = int(input())

array = []

for i in range(1,n+1):
    
    array.append(i)


permutation = permutations(array)

perm = list(permutation)

arraycheck = []

arraycheck1=[]

odd = []

for i in perm:
    arraycheck.append(i)

    arraycheck1 = arraycheck[0]

    arraycheck.clear()

    for i in arraycheck1:
        if i%2>0:
            odd.append(i)
    
    flag = 0

    test_list1 = odd[:]
    test_list1.sort()
    if (test_list1 == odd):
        flag = 1
      
    # printing result
    if (flag) :
        print ("Yes, Odd numbers sorted")
        print(arraycheck1)
        odd.clear()
    else :
        print ("No, List is not sorted.")
        odd.clear()









    
