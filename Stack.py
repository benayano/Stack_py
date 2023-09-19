from Node import Node


class Stack:

    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def __str__(self):
        current = self.head.next
        out = ''
        while current:
            out += str(current.data) + ' -> '
            current = current.next
        return out[:-3]

    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        top = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return top.data

    def top(self):
        if self.isEmpty():
            raise Exception("the Stack is empty empty ")
        return self.head.next.data

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def isNotEmpty(self):
        return self.isEmpty() == False
