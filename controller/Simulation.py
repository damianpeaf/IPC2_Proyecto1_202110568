from data.doublyLinkedListWithIndex import DoublyLinkedListWithIndex
from data.matrix import SquareMatrix
from logic.logic import detectDisease, generateNextState


class Simulation():

    def __init__(self, patientRegister):
        # * Register
        self.patientRegister = patientRegister

        # * History
        self.history = DoublyLinkedListWithIndex()

        self.history.insertAtEnd(self.patientRegister.initialState)

        # * Diseases

        self.maxPeriodsUntilDisease = int(patientRegister.periods)

        # initial pattern
        self.initialStatePatternDetected = False
        self.initialStatePatternPeriod = 0

        # later pattern
        self.laterStatePatternDetected = False
        self.laterStatePatternOcurrence = 0
        self.laterStatePatternPeriod = 0

        # Type
        self.diseaseType = ""

        # * actual state
        self.actualState = self.history.getElement(0)

        # * other stats
        self.periodsLeft = self.maxPeriodsUntilDisease
        self.actualPeriod = 0
        self.healthyCells = 0
        self.infectedCells = 0

        # * end simulation
        self.simulationEnd = False

        # * Refresh stats
        self.countCells()

    def nextState(self):

        # Doesnt exist next state
        if self.history.getElement(self.actualPeriod + 1) == None:
            if not self.simulationEnd:
                # * New matrix
                newState = generateNextState(self.actualState)
                self.history.insertAtEnd(newState)

                # * Next period
                self.actualState = self.history.getElement(self.actualPeriod +
                                                           1)
                self.actualPeriod += 1

                # * Detect disease
                self.lookForDiseases()
                self.hasSimulationEnded()
                self.periodsLeft -= 1

        # Already exists state
        else:
            self.actualState = self.history.getElement(self.actualPeriod + 1)
            self.actualPeriod += 1
            self.periodsLeft -= 1

    def prevState(self):
        if self.actualPeriod - 1 < 0:
            return

        self.actualState = self.history.getElement(self.actualPeriod - 1)
        self.actualPeriod -= 1
        self.periodsLeft += 1

    def runAllStates(self):
        while not self.simulationEnd:
            self.nextState()

    def hasSimulationEnded(self):
        self.simulationEnd = self.laterStatePatternDetected or self.initialStatePatternDetected or (
            self.actualPeriod == self.maxPeriodsUntilDisease)

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
            diseases += f"Patron inicial repetido cada (N): {str(self.initialStatePatternPeriod)}\n\n"
        else:
            diseases += "No se ha detectado que se repita el patron inicial\n\n"

            if self.laterStatePatternDetected:
                diseases += f"Patron posterior empieza (N): {str(self.laterStatePatternOcurrence)} \n Patron poseterior repetido cada (N1): {str(self.laterStatePatternPeriod)}\n\n"
            else:
                diseases += "No se ha detectado que se repita un patron posterior\n\n"

        diseases += f"Tipo de enfermedad: {self.diseaseType}\n"

        stats = ""

        if self.periodsLeft <= 0:
            stats += "Han pasado el limite de periodos restantes\n"
        else:
            stats += f"Periodos restantes: {str(self.periodsLeft)}\n"

        stats += f"Periodo actual : {str(self.actualPeriod)} \n Celulas sanas : {str(self.healthyCells)} \n Celulas infectadas : {str(self.infectedCells)}"

        patientInfo = f"Nombre : {self.patientRegister.name}\n Edad : {str(self.patientRegister.age)}"

        return {"diseases": diseases, "stats": stats, "patient": patientInfo}

    def lookForDiseases(self):

        # a. Que el patrón inicial se repita siempre después de “N” períodos, en este caso la enfermedad produce un caso grave. Si “N” es igual a 1, entonces, el paciente morirá a causa de la enfermedad, ya que ésta será incurable.
        initialMatrix = self.history.getElement(0)
        for i in range(0, self.history.lenght):

            if i == 0:
                continue

            if SquareMatrix.isMatrixEqual(initialMatrix,
                                          self.history.getElement(i)):
                self.initialStatePatternDetected = True
                self.initialStatePatternPeriod = i

                if self.initialStatePatternPeriod == 1:
                    self.diseaseType = "mortal"
                else:
                    self.diseaseType = "grave"

                return

        # b. Que algún patrón, distinto al patrón inicial, se repita luego de “N” períodos cada “N1” períodos, en este caso la enfermedad producirá un caso grave. Si “N1” es igual a 1, entonces, el paciente morirá a causa de la enfermedad, ya que ésta será incurable, en caso de que “N1” es mayor que 1, la enfermedad será grave.
        for i in range(0, self.history.lenght):

            if i == 0:
                continue

            patternToFind = self.history.getElement(i)

            for j in range(i + 1, self.history.lenght):
                if SquareMatrix.isMatrixEqual(patternToFind,
                                              self.history.getElement(j)):
                    self.laterStatePatternDetected = True
                    self.laterStatePatternOcurrence = i
                    self.laterStatePatternPeriod = j - i

                    if self.initialStatePatternPeriod == 1:
                        self.diseaseType = "mortal"
                    else:
                        self.diseaseType = "grave"

                    return

        self.diseaseType = "leve"
