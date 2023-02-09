def mini(ary):
    n = len(ary)
    for i in range(n-1):
        idx = i
        for j in range(i+1,n):
            if ary[idx] > ary[j]:
                idx = j
        tmp = ary[i]
        ary[i] = ary[idx]
        ary[idx] = tmp

for i in range(len(arr2)):
    for j in range(lmne(arr2[i])):
        arr1.append(arr2[i][j])

