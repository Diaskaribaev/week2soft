from math import factorial


x  = float(input())
n  = int(input())

total = 1+x/2

multiply = 2
for q in range(2,n+1):
            multiply *= q *2

for i in range(1,n+1):
    if i%2>0:
        
        total += (2*i-3)*x/factorial(multiply)
    elif i%2==0:
        total -= (2*i-3)*x/factorial(multiply) 



print(total)

