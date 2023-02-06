import random
import math

class Node():
    def __int__(self):
        self.data = None
        self.link = None

#답지를 보니 print 함수와 넣는 함수를 만들어야 함.

def printNode(start):
    current = start
    if current == None: #그냥 종료하는 것.
        return
    print("상가 이름 : ", current[0])
    print("상가 거리 : ", math.sqrt(current[1] ** 2 + current[2] ** 2))
    while current.link != start:
        #관련 내용을 주어야 겠네/
        current = current.link
        print("상가 이름 : ", current[0])
        print("상가 거리 : ", math.sqrt(current[1]**2 + current[2]**2))

def makingNode(store):
    global head
    node = Node()
    node.data = store

    #노드가 없으면?
    if head == None:
        head = node
        node.link = head
        return

    x,y = store[1:]
    dist = math.sqrt(x**2 + y**2)

    #맨처음에 넣기
    hx,hy = head[1:]
    hdist = math.sqrt(hx**2 + hy**2)

    if dist < hdist:
        node.link = head
        last = head
        #last 찾기
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    #중간에 넣기.
    current = head
    while current.link != head:
        pre = current
        current = current.link
        cx, cy = current[1:]
        cdist = math.sqrt(cx**2 + cy ** 2)

        if dist < cdist:
            node.link = current
            pre.link = node
            return

    #끝에 넣기, 위에서 마지막까지 보냈으니까.
    current.link = node
    node.link = head


#상가 입력란,
firstName= "A"
stores = []
for i in range(10):
    store = (firstName, random.randint(1,50),random.randint(1,50))
    stores.append(store)
    firstName = chr(ord(firstName) + 1)

for store in stores:
    makingNode(store)
printNode(head)



