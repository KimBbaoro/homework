def isFull():
    global SIZE, top, stack
    if top >= SIZE-1:
        return True
    return False

def isEmpty():
    global SIZE, top, stack
    if top <=-1:
        return True
    return False

def push(data):
    global SIZE, top, stack

    if isFull():
        return
    top +=1
    stack[top] = data

def pop():
    global SIZE, top, stack

    if isEmpty():
        return
    data = stack[top]
    top-=1
    return data

def peek():
    global SIZE, top, stack
    if isEmpty():
        return
    return stack[top]

SIZE =10
stack = [None] * SIZE
top -=1

stones = ["빨","파","초","노","보","주"]
print("과자 집에 가는 길 : ", stone)
for stone in stones:
    push(stone)
    print(stone, "-->", end='')
print("과자집")

print("집 가는 길 ---> ", end='')
for _ in range(SIZE):
    stone=pop()
    print(stone, "--->", end=' ')
print("우리집")
