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

#queue를 돌면서 확인하겠네.
def calTime():
    global SIZE, queue, front, rear
    timeSum = 0
    #print("front : ",(front+1)%SIZE)
    #print("rear : ",(rear+1)%SIZE)

    for i in range((front+1) % SIZE, (rear+1)%SIZE):
        # print("flag")
        # print(i)
        timeSum += queue[i][1]
    return timeSum


waits = [("사용", 9), ("고장",3), ("환불", 4), ("환불" , 4), ("고장", 3)]
SIZE = len(waits)+1

queue = [None] * SIZE
front = rear = 0

for wait in waits:
    # print("queue : ", queue)
    print("대기시간 : ", calTime())
    print("queue : ",queue)
    enQueue(wait)
    print()

print("마지막 queue : ", queue)
print("프로그램 종료!")




