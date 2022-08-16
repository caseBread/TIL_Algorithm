import sys
ip = sys.stdin.readline

s = ip()

t = set()

for i in range(len(s)) :
    for j in range(i+1,len(s)) :
        t.add(s[i:j])

print(len(t))