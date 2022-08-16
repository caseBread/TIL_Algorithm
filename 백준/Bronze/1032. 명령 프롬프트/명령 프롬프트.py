t = int(input())
arr = []
maxLen = 0
for _ in range(t) :
    x = input()
    arr.append(x)
    maxLen = max(maxLen, len(x))

result = ""
for i in range(maxLen) :
    same = True
    for j in range(len(arr)) :
        if (j == 0) :
            sameChar = arr[j][i]
        else :
            if sameChar != arr[j][i] :
                same = False
    if (same) :
        result += arr[j][i]
    else :
        result += "?"



print(result)