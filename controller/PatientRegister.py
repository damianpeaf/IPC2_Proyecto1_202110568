from data.doublyLinkedListWithIndex import DoublyLinkedListWithIndex


class PatientRegister(object):

    def __init__(self, name, age, periods, cellDimension, initialMatrix):
        self.name = name
        self.age = age
        self.periods = periods
        self.cellDimension = cellDimension
        self.initialState = initialMatrix
