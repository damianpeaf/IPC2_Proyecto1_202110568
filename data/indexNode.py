from data.node import Node


class IndexNode(Node):

    def __init__(self, data=None, rowIndex=None, nextNode=None, prevNode=None):
        super().__init__(data, nextNode, prevNode)
        self.rowIndex = rowIndex
