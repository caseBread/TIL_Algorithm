import sys
ip = sys.stdin.readline

n,m = map(int,ip().split())

a = list(map(int,ip().split()))
b = list(map(int,ip().split()))

t = len(set(a)&set(b))

print(len(a)+len(b)-(t*2))