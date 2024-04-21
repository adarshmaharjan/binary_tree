"""

Algorithm:

Starting at the root, find the deepest and rightmost node in the binary tree and the node which we want to delete. 
Replace the deepest rightmost node’s data with the node to be deleted. 
Then delete the deepest rightmost node.

"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"{self.data}"


def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


# delete the given deepest node


def deleteDeepest(root, d_node):
    q = []
    q.append(root)

    while len(q):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)


#  delete element in binary tree


def deletion(root, key):
    if root == None:
        return None

    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root

    key_node = None
    q = []
    q.append(root)
    temp = None

    # find a node to be deleted
    while len(q):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    # replace the delete node with rigtmost node
    if key_node:
        x = temp.data
        key_node.data = x
        deleteDeepest(root, temp)
    return root


if __name__ == "__main__":
    root = Node(13)
    root.left = Node(12)
    root.left.left = Node(4)
    root.left.right = Node(19)
    root.right = Node(10)
    root.right.left = Node(16)
    root.right.right = Node(9)

    print("The tree before the deletion: ", end=" ")
    inorder(root)
    key = 12
    root = deletion(root, key)
    print()
    print("The tree after the deletion: ", end="")
    inorder(root)
