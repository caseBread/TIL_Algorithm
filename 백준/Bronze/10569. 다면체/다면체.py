import sys
ip = sys.stdin.readline

t=int(ip())
for _ in range(t) :
    v,e=map(int,ip().split())
    print(2-v+e)