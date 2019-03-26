class node(object):
    value= 0
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

def agregarNodo(root, newVal):
    tempNode = node(newVal)
    if tempNode.value < root.value:
        if root.left == None:
            root.setLeft(tempNode)
        else:
            agregarNodo(root.left, newVal)
    else:
        if root.right == None:
            root.setRight(tempNode)
        else:
            agregarNodo(root.right, newVal)

def impresion (root, arbol):
    arbol.append(str(root.value))

    left = []
    right = []
    if (root.left != None):
        left.append(impresion(root.left, []))
    if (root.right != None):
        right.append(impresion(root.right, []))

    arbol.append(left)
    arbol.append(right)
    return arbol

nums = [6, 7, 10, 11, 5, 3, 2]

root = node(nums[0])
for x in range(1,len(nums)):
    agregarNodo(root, nums[x])

arbol= impresion(root, [])
print(arbol)



