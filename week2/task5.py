from itertools import permutations



n = int(input())

array = []

for i in range(1,n+1):
    
    array.append(i)


permutation = permutations(array)

perm = list(permutation)

arraycheck = []

arraycheck1=[]

even = []

for i in perm:
    arraycheck.append(i)

    arraycheck1 = arraycheck[0]

    arraycheck.clear()

    for i in arraycheck1:
        if i%2==0:
            even.append(i)
    
    flag = 0

    test_list1 = even[:]
    test_list1.sort()
    test_list1.reverse()
    if (test_list1 == even):
        flag = 1
      
    # printing result
    if (flag) :
        print ("Yes, Even numbers on descending order")
        print(arraycheck1)
        even.clear()
    else :
        print ("No, List is not sorted.")
        even.clear()









    
