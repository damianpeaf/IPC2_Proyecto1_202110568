from data.bodyNode import BodyNode
from data.doublyLinkedList import DoublyLinkedList
from data.indexNode import IndexNode


class SquareMatrix(object):

    def __init__(self, dimension=1):
        self.dimension = dimension
        self.initMatrix()

    def initMatrix(self):
        self.indices = DoublyLinkedList()
        for i in range(0, self.dimension):

            row = DoublyLinkedList()
            for j in range(0, self.dimension):
                row.insertAtEnd(BodyNode(None, i, j))

            self.indices.insertAtEnd(IndexNode(row, i))

    def isInvalidIndex(self, row, column):
        return row >= self.dimension or column >= self.dimension

    def getElement(self, row, column):
        if self.isInvalidIndex(row, column):
            print('Not valid index')
            return

        indexToRead = self.indices.tail
        while indexToRead:

            # Same rowIndex
            if indexToRead.rowIndex == row:
                # Reads that row
                rowElement = indexToRead.data.tail

                while rowElement:
                    # Same column Index
                    if (rowElement.column == column):
                        return rowElement.data
                    rowElement = rowElement.nextNode

            indexToRead = indexToRead.nextNode

    def setElement(self, row, column, data):
        if self.isInvalidIndex(row, column):
            print('Not valid index')
            return

        indexToRead = self.indices.tail
        while indexToRead:

            # Same rowIndex
            if indexToRead.rowIndex == row:
                # Reads that row
                rowElement = indexToRead.data.tail

                while rowElement:
                    # Same column Index
                    if (rowElement.column == column):
                        rowElement.data = data
                        return
                    rowElement = rowElement.nextNode

            indexToRead = indexToRead.nextNode

    def readAllMatrix(self):
        indexToRead = self.indices.tail

        while indexToRead:

            rowElement = indexToRead.data.tail

            rowText = " |"
            while rowElement:
                rowText += " " + str(rowElement.data) + " |"
                rowElement = rowElement.nextNode

            print(rowText)

            indexToRead = indexToRead.nextNode

    @staticmethod
    def isMatrixEqual(matrix1, matrix2):

        if (matrix1.dimension != matrix2.dimension):
            return False

        for i in range(0, matrix1.dimension):
            for j in range(0, matrix1.dimension):
                if (matrix1.getElement(i, j) == matrix2.getElement(i, j)):
                    pass
                else:
                    return False

        return True
