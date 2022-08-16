import sys
ip = sys.stdin.readline

n,m = map(int,ip().split())

s = []

for _ in range(n) :
    s.append(ip().rstrip())

for _ in range(m) :
    t = ip().rstrip()
    if 48 <= ord(t[0]) <= 57 :
        print(s[int(t)-1])
    else :
        print(s.index(t)+1)