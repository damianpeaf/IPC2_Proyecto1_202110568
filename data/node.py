
from sqlite3 import DateFromTicks


class Node(object):

    def __init__(self, data=None, nextNode=None, prevNode=None):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode
