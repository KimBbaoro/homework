
stores=[
    [1,2],
    [0,2,3],
    [0,1,3],
    [1,2,4],
    [3]
]

weight = [30,60,10,90,40]
ans = []
nameList = ["gs", "cu", "7", "mini", "24"]
visited = [False] * len(stores)
def dfs(stores, v, visited):
    global maxCount
    visited[v] = True
    tmp = weight[v]
    if tmp > maxCount:
        maxCount = tmp
        ans.append(v)

    for store in stores[v]:
        if not visited[store]:
            dfs(stores, store, visited)


maxCount = 0

dfs(stores,0,visited)
print(nameList[ans[-1]],end = ' ')
print(maxCount)

