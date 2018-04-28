import sys
import math

a = 1234567891011
b = a
c = 1
min = sys.maxsize

for x in range(int(math.sqrt(a)),2,-1):
    if a % x == 0:
        c = x
        b = a / x
    if b + c < min:
        print(b)
        print(c)
        min = b + c

print("Minimum Value:" , min)





