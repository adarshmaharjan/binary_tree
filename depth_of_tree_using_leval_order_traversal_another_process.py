class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    q = []
    q.append(root)
    height = 0

    while q:
        nodeCount = len(q)
        while nodeCount > 0:
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right) 
            nodeCount -= 1
        height += 1
    return height


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(f"Height: {height(root)}")
