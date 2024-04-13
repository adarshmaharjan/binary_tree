
class Node:
    def __init__(self) :
        self.key: 0
        self.left = None
        self.right = None

    def __repr__(self):
        return f"key: {self.key}"

def newNode(key):
    temp = Node()
    temp.key = key
    temp.left = None
    temp.right = None
    return temp


def height(root):
    depth = 0
    q = []

    q.append(root)
    
    q.append(None)
    
    while(len(q)>0):
        print(q)
        temp = q[0]
        print(temp)
        q = q[1:]

        if(temp is None):
            depth+=1
        if temp is not None:
            if(temp.left):
                q.append(temp.left)
            if(temp.right):
                q.append(temp.right)
        elif(len(q)>0):
            q.append(None)
    return depth


root = newNode(1)

root.left = newNode(2)
root.right = newNode(3)

root.left.left = newNode(4)
root.left.right = newNode(5)


print(f"Height(Depth) of tree is: {height(root)}")
