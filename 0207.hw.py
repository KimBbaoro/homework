def isQueueFull():
    global SIZE, queue, front, rear
    if rear !=SIZE-1:
        return False
    elif rear == SIZE-1 and front ==-1:
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            #print("test queue : ",queue)
            queue[i] = None
        front -=1
        rear -=1
        return False



def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print("꽉 찼음")
        return
    else:
        rear = (rear+1)%SIZE
        queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("비어있음")
        return
    else:

        front = (front+1)%SIZE
        data = queue[front]
        queue[front] = None

        #칸 당겨야지
        for i in range(front +1, rear+1):
            queue[i-1] = queue[i]
            queue[i] = None
        front -=1
        rear -=1

        return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("비어있음")
        return
    return queue[(front +1)%SIZE]

SIZE = 5
queue = [None] * SIZE
front = rear = -1

enQueue("정국")
enQueue("뷔")
enQueue("지민")
enQueue("진")
enQueue("슈가")
print("대기 줄 상태 : ", queue)

for _ in range(rear+1):
    print(deQueue(), "님 식당에 들어감")
    print("대기줄 상태 확인 : ", queue)
print("영업 끝")
