def bin_Search(arr, fData):
    global cnt
    start = 0
    end = len(arr)-1

    while start<=end:
        cnt +=1
        mid = (start + end)//2
        if arr[mid] == fData:
            return mid
        elif arr[mid] > fData:
            end = mid-1
        elif arr[mid] < fData:
            start = mid +1
        else:
            return -1

def seqSearch(ary, fData):
    global cnt
    pos = -1
    for i in range(len(ary)):
        cnt +=1
        if ary[pos] == fData:
            pos = i
            break
    return pos

import random


