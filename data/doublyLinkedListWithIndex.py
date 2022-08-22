from data.NumberNode import NumberNode
from data.doublyLinkedList import DoublyLinkedList


class DoublyLinkedListWithIndex(DoublyLinkedList):

    def __init__(self):
        super().__init__()

    def insertAtEnd(self, data):

        newNode = NumberNode(data, self.lenght)
        # Empty list
        if self.isEmpty():
            self.tail = self.head = newNode
        # Has nodes
        else:
            olderHead = self.head
            self.head = olderHead.nextNode = newNode
            self.head.prevNode = olderHead
        self.lenght += 1

    def getElement(self, index):

        nodeToRead = self.tail
        while nodeToRead:
            if nodeToRead.index == index:
                return nodeToRead.data
            nodeToRead = nodeToRead.nextNode

        return None
