def scoreSort(ary):
    n = len(ary)
    for end in range(1,n):
        for cur in range(end, 0, -1):
            if ary[cur-1][1] > ary[cur][1]:
                ary[cur - 1][1], ary[cur][1] = ary[cur][1],ary[cur-1][1]
    return ary

arr = []
arr = scoreSort(arr)
for i in range(len(arr)//2):
    print(arr[i][0], arr[len(arr)-1][0])