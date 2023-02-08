city_name = ["서울", "뉴옥", "방콕", "런던", "파리", "북경"]

graph = [
    (80, 0, 1),
    (10, 0, 5),
    (40, 1, 5),
    (50, 5, 2),
    (70, 1, 2),
    (30, 3, 2),
    (20, 2, 4),
    (60, 3, 4)
]
graph.sort(key=lambda x:x[0])

parent = list(range(len(city_name)))
def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(city):
    if city == parent[city]:
        return city
    parent[city] = find(parent[city])
    return parent[city]
sum =0
new_graph = []
for w,a,b in graph:
    if find(a) != find(b):
        union(a,b)
        new_graph.append((a,b))
        sum +=w
for a,b in new_graph:
    print(city_name[a] + "&" + city_name[b], end=' ')
print()
print(sum)
