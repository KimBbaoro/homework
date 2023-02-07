import random
class TreeNode():
    def __init__(self):
        self.data= None
        self.left = None
        self.right = None

node1 = TreeNode()
node1.data = "화사"

node2 = TreeNode()
node2.data = "솔라"


memo = []
datas = ["바나나맛", "레쓰비", "츄파", "도시락", "삼다수", "콜라","삼각"]
sells = [random.choice(datas) for _ in range(20)]

node = TreeNode()
node.data = sells[0]
root = node
memo.append(node)
for sell in sells[1:]:
    node = TreeNode()
    node.data = sell
    current = root
    while True:
        #들어있으면
        print("현재 : ", current)
        print("현재 값 : ", current.data)
        if sell == current.data:
            break

        if sell < current.data:
            if current.data == None:
                current.left = node
                memo.append(node)
                break
            current = current.left
        else:
            if current.data == None:
                current.right = node
                memo.append(node)
                break
            current = current.right

def preOrder(node):
    if node == None:
        return
    print(node.data, end ='')
    preOrder(node.left)
    preOrder(node.right)

preOrder(root)