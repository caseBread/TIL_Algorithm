import sys
ip = sys.stdin.readline

n=int(ip())
s=ip().strip("\n")

res=0
for i in range(len(s)) :
    res += (ord(s[i])-96)*(31**i)

print(res)