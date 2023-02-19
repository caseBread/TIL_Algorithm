import sys
ip = sys.stdin.readline

c = [[10],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]

t = int(ip())
for _ in range(t) :
    a,b = map(int,ip().split())
    print(c[a%10][b%(len(c[a%10]))-1])