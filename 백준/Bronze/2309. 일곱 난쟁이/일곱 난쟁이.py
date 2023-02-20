import sys
ip = sys.stdin.readline

arr=[]
for _ in range(9) :
    arr.append(int(ip()))
arr.sort()
summ = sum(arr)
for i in range(9) :
    for j in range(9) :
        if j != i :
            if summ-arr[j]-arr[i] == 100 :
                for k in range(len(arr)) :
                    if k == j or k == i :
                        continue
                    print(arr[k])
                exit()