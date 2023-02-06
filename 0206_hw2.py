#2중 노드

class Node():
    def __init__(self):
        self.data = None
        self.preLink = None
        self.nextLink = None


def printNode(start):
    current = start
    if current.nextLink == None:
        return

    #정방향
    print("정방향 --> : ", end='')
    print(current.data,end='')
    while current.nextLink != None:
        current = current.link
        print(current.data, end = '')
    print()

    print("역방향 --> ", end= '')
    print(current.data, end='')
    while current.preLink != None:
        current = current.preLink
        print(current.data, end='')
    print()

head = None
def makingNode(name):
    global head
    node = Node()
    node.data = name
    #첫 데이터 만들기
    if head==None:
        head = node

    pre = node
    node = Node()
    node.data = name
    pre.nextLink = node
    node.preLink = pre


names = ["다현", "정연", "쯔위", "사나", "지효"]
for name in names:
    makingNode(name)

printNode(names[0])
