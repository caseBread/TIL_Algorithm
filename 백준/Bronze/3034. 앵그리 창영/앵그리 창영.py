import sys
ip = sys.stdin.readline

n,w,h = map(int,ip().split())
for _ in range(n) :
    if int(ip())**2<=w**2+h**2:print("DA")
    else :print("NE")
