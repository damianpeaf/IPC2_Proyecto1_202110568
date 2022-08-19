from data.doublyLinkedListWithIndex import DoublyLinkedListWithIndex
from logic.logic import generateNextState


class Simulation():

    MAX_PERIODS = 10000

    def __init__(self, patientRegister):
        # * Register
        self.patientRegister = patientRegister

        # * History
        self.history = DoublyLinkedListWithIndex()

        self.history.insertAtEnd(self.patientRegister.initialState)

        # * Diseases

        # initial pattern
        self.initialStatePatternDetected = False
        self.initialStatePatternPeriod = 0

        # later pattern
        self.laterStatePatternDetected = False
        self.laterStatePatternOcurrence = 0
        self.laterStatePatternPeriod = 0

        # Type
        # ? Create a new class
        self.diseaseType = ""

        # * actual state
        self.actualState = self.history.getElement(0)

        # * other stats
        self.actualPeriod = 0
        self.healthyCells = 0
        self.infectedCells = 0

        # * end simulation
        self.simulationEnd = False

        # * Refresh stats
        self.countCells()

    def nextState(self):
        # * New matrix
        newState = generateNextState(self.actualState)
        self.history.insertAtEnd(newState)

        # * Next period
        self.actualState = self.history.getElement(self.actualPeriod + 1)
        self.actualPeriod += 1

        # * Detect disease

    def runAllStates():
        pass

    def lookForDiseases():
        pass

    def countCells(self):

        matrix = self.actualState

        infected = 0
        healthy = 0
        for i in range(0, matrix.dimension):
            for j in range(0, matrix.dimension):
                if matrix.getElement(i, j):
                    infected += 1
                else:
                    healthy += 1

        self.healthyCells = healthy
        self.infectedCells = infected

    def info(self):
        self.countCells()

        diseases = ""

        if self.initialStatePatternDetected:
            diseases += f"Patron inicial repetido cada : {str(self.initialStatePatternPeriod)}\n"
        else:
            diseases += "No se ha detectado que se repita el patron inicial\n"

        if self.laterStatePatternDetected:
            diseases += f"Patron posterior empieza : {str(self.laterStatePatternOcurrence)} \n Patron poseterior repetido cada : {str(self.later)}\n"
        else:
            diseases += "No se ha detectado que se repita un patron posterior\n"

        stats = f"Periodo actual : {str(self.actualPeriod)} \n Celulas sanas : {str(self.healthyCells)} \n Celulas infectadas : {str(self.infectedCells)}"

        patientInfo = f"Nombre : {self.patientRegister.name}\n Edad : {str(self.patientRegister.age)}"

        return {"diseases": diseases, "stats": stats, "patient": patientInfo}
