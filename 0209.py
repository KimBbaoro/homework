import random
import time

def select(ary):
    n = len(ary)
    for i in range(0,n-1):
        idx = i
        for k in range(i+1, n):
            if ary[idx] > ary[k]:
                idx = k

        tmp = ary[i]
        ary[i] = ary[idx]
        ary[idx] = tmp

    return ary

def quick(arr,start, end):
    if end <= start:
        return
    low = start
    high = end

    pivot = arr[(low + high) //2]
    while low <=high:
        while arr[low] < pivot:
            low +=1
        while arr[high] > pivot:
            high -=1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low+=1
            high +=1
    mid = low

    quick(arr, start, mid-1)
    quick(arr, mid, end)