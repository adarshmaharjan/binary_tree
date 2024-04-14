from platform import node
from re import A


class newNode:
    def __init__(self, data) -> None:
        self.key = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"{self.key}"


def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.key, end="->")
    inorder(temp.right)


def insert(temp, key):
    if not temp:
        root = newNode(key)
        return
    q = []
    q.append(temp)

    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)


root = newNode(1)
root.left = newNode(2)
root.left.left = newNode(3)
root.right = newNode(4)
root.right.left = newNode(5)
root.right.right = newNode(8)


print("In order traversal before insertion", end="\n")
inorder(root)

key = 12
insert(root, key)
print("\n")
print("Inorder traversal after insertion", end="\n")
inorder(root)
