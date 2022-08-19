class Simulation():

    MAX_PERIODS = 10000

    def __init__(self, patientRegister):
        # * Register
        self.patientRegister = patientRegister

        # * Diseases

        # initial pattern
        self.initialStatePatternDetected = False
        self.initialStatePatternPeriod = 0

        # later pattern
        self.laterStatePatternDetected = False
        self.laterStatePatternOcurrence = 0
        self.laterStatePatternPeriod = 0

        # * actual state
        self.actualState = self.patientRegister.history.getElement(0)

        # count cell types
        counter = self.countCells(self.actualState)

        # * other stats
        self.actualPeriod = 0
        self.healthyCells = counter["healthy"]
        self.infectedCells = counter["infected"]

        # * end simulation
        self.simulationEnd = False

    def nextState():
        pass

    def runAllStates():
        pass

    def lookForDiseases():
        pass

    def countCells(self, matrix):
        infected = 0
        healthy = 0
        for i in range(0, matrix.dimension):
            for j in range(0, matrix.dimension):
                if matrix.getElement(i, j):
                    infected += 1
                else:
                    healthy += 1
        return {"infected": infected, "healthy": healthy}

    def info(self):
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

        return {"diseases": diseases, "stats": stats}
