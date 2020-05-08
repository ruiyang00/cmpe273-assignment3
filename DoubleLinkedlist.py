
class DoubleLinkedlist():
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.tail.next = None
        self.head.pre = None
        self.size = 0

    def addFront(self, value):
        node = Node(value)
        # print(node.value)
        self.head.next.pre = node
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node
        self.size += 1

    def removeTail(self):
        if self.tail.pre.pre != None:
            self.tail.pre.pre.next = self.tail
            self.tail.pre = self.tail.pre.pre
            self.size -= 1

    def get_size(self):
        return self.size

    def getTail(self):
        return self.tail.pre


class Node():
    def __init__(self, value):
        self.pre = None
        self.next = None
        self.value = value

