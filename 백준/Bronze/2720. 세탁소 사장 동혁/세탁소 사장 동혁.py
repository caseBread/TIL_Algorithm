import sys
ip = sys.stdin.readline

t=int(ip())
for _ in range(t) :
  n = int(ip())
  res=[]
  
  res.append(n//25)
  n%=25
  res.append(n//10)
  n%=10
  res.append(n//5)
  n%=5
  res.append(n)
  
  for i in res :
    print(i,end=" ")
  print()