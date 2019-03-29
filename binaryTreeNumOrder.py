import turtle
from tkinter import *


class node(object):
    val = 0
    left = None
    right = None

    def __init__(self, val):
        self.val = val

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node


def agregarNodo(root, newVal):
    tempNode = node(newVal)
    if tempNode.val < root.val:
        if root.left == None:
            root.setLeft(tempNode)
        else:
            agregarNodo(root.left, newVal)
    else:
        if root.right == None:
            root.setRight(tempNode)
        else:
            agregarNodo(root.right, newVal)

def height(root):
    return 1 + max(height(root.left), height(root.right)) if root else -1


def addTree():
    input = iterEntry.get()
    nums = (input[1:-1])
    nodes = nums.split(",")
    root = node(int(nodes[0]))
    for x in range(1, len(nodes)):
        agregarNodo(root, int(nodes[x]))
    window.destroy()
    turtleDraw(root)


def turtleDraw(root):
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    t=turtle.Turtle()
    t.speed(0);
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


window = Tk()
window.title("Page Break")
window.geometry("500x300")

topFrame = Frame(window)
topFrame["pady"] = 10
topFrame.pack(side=TOP)

accion = Label(topFrame, text="Arbol en forma:{1,2...n}")
accion.pack(side=TOP)

iterEntry = Entry(topFrame)
iterEntry.pack(side=TOP)

btdir1 = Button(topFrame, text="Dibujar Arbol", command=addTree)
btdir1.pack(side=TOP)

window.mainloop()
