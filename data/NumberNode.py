from data.node import Node


class NumberNode(Node):

    def __init__(self, data=None, index=None, nextNode=None, prevNode=None):
        self.index = index
        super().__init__(data, nextNode, prevNode)