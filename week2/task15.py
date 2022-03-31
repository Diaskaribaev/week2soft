
n = int(input())
print("-----------------------------------")
if n ==1:
    print('1')
elif n == 2:
    print('1')
    print('2') 
elif n == 3:
    print('1')
    print('2')
    print('3')
else:
    print('1')
    print('2')
    print('3')



a1 = 1 
a2 = 2
a3 = 3

for i in range(4,n+1):
               
        a  =  a3 + a2 - 2*a1
        print(a)
        a3 = a
        a2 = a3
        a1 = a2