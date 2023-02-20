def bin_Search(arr, fData):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = (start + end)//2
        if arr[mid] == fData:
            return mid
        elif arr[mid] > fData:
            end = mid-1
        elif arr[mid] < fData:
            start = mid +1
        else:
            return -1

import random
dataArr = ["바나나맛 우유", "레쓰비", "츄파", "도시락", "삼다수", "코카콜라", "삼각김밥"]
sellArr = [random.choice(dataArr for _ in range(20))]

sellP = list(set(sellArr.sort()))

cntList = []

for p in sellP:
    cnt = 0
    pos = 0
    while pos!=-1:
        pos = bin_Search(sellArr, p)
        if pos!=-1:
            cnt+=1
            del(sellArr[pos]) #계속 없애기
    cntList.append((p, cnt))

print()
print(cntList)