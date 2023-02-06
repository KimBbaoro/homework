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

with open("____.txt", 'r', encoding='UTF8') as rfp
    lineAry = rfp.readlines()

print("원본")
for line in lineAry:
    push(line)
    print(line, end=' ')
print()

print("거꾸로")
while True:
    line = pop()
    if line == None:
        break
