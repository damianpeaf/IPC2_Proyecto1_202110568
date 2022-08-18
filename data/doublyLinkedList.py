from data.node import Node


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def isEmpty(self):
        return self.tail == None

    def insertAtEnd(self, node):

        newNode = node
        # Empty list
        if self.isEmpty():
            self.tail = self.head = newNode
        # Has nodes
        else:
            olderHead = self.head
            self.head = olderHead.nextNode = newNode
            self.head.prevNode = olderHead

        self.lenght += 1

    def insertAtStart(self, node):
        newNode = node

        if self.isEmpty():
            self.tail = self.head = newNode
        else:
            newNode.nextNode = self.tail
            self.tail.prevNode = newNode
            self.tail = newNode

        self.lenght += 1

    def readAtStart(self):
        # First node to read
        nodeToRead = self.tail
        while nodeToRead:
            print(nodeToRead.data)
            nodeToRead = nodeToRead.nextNode

    def deleteAtStart(self):
        if self.isEmpty():
            pass
        elif self.tail.nextNode == None:
            self.tail = self.head = None
            self.lenght = 0
        else:
            self.tail = self.tail.nextNode
            self.tail.prevNode = None
            self.lenght -= 1

    def deleteAtEnd(self):
        if self.isEmpty():
            pass
        elif self.tail.nextNode == None:
            self.tail = self.head = None
            self.lenght = 0
        else:
            self.head = self.tail.prevNode
            self.head.nextNode = None
            self.lenght -= 1
