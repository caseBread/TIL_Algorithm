import sys
import math
ip = sys.stdin.readline

n = int(ip())
z = math.floor((n*15/100)+0.5)

if (n == 0) :
    print(0)
    exit()

arr  = []
for i in range(n) :
    arr.append(int(ip()))

arr.sort()
print(math.floor(sum(arr[z:n-z])/(n-(z*2))+0.5))