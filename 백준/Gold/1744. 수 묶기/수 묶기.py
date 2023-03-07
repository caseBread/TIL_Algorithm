import sys
ip = sys.stdin.readline

n=int(ip())
arr=[]
neg_arr=[]
zeroCnt = 0
for _ in range(n) :
  temp = int(ip())
  if temp > 0 :
    arr.append(temp)
  elif temp < 0 :
    neg_arr.append(temp)
  else :
    zeroCnt += 1

arr.sort(reverse=True)
neg_arr.sort()
zeroArr = [0]*zeroCnt
arr = arr + neg_arr + zeroArr

result = 0
i = 0
while i < n :

  if arr[i] == 1 :
    result += 1
    i += 1
  elif i+1 < n and arr[i] > 0 and arr[i+1] <= 0 :
    result += arr[i]
    i += 1
  else :
    if i+1 < n and arr[i+1] != 1 :
      result += arr[i]*arr[i+1]
      i += 2
    else :
      result += arr[i]
      i += 1

print(result)