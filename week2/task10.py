from math import sin

n,a,b = int(input()),int(input()),int(input())

h = round((b-a)/n)

print(h)


print ("--------------------------")

print(sin(a))

for x in range (1,h):
    print(1 - sin(a + x*h))

