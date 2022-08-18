from data.node import Node


class BodyNode(Node):
    def __init__(self, data=None, row=None, column=None, nextNode=None, prevNode=None):
        super().__init__(data, nextNode, prevNode)
        self.row = row
        self.column = column
