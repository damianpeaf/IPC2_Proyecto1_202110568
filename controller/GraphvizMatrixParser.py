from os import system


class GraphvizMatrixParser():

    def __init__(self, matrix, period):
        self.matrix = matrix
        self.period = str(period)
        self.parseToSrtDot()
        self.generateFile()

    def generateFile(self):
        try:
            f = open(f"./dot/Grill{self.period}.dot", "x")
            f.write(self.dotStr)
            f.close()

            print('Archivo generado')

            return True

        except Exception as e:
            print(e)
            print('eeeeeeeeeeee')
            return False

    def parseToSrtDot(self):

        self.dotStr = ""

        # * Init
        self.dotStr += f"digraph P{str(self.period)}" + "{\n"
        self.dotStr += "node [shape=box, nodesep=1, fillcolor=blue, style=filled]\n"
        self.dotStr += "subgraph \"periodo" + self.period + "\" {\n"
        self.dotStr += "edge[dir=\"both\"]\n"
        self.dotStr += "Label_" + self.period + "[label = \"periodo " + self.period + " \", style=rounded, pos=\"" + str(
            self.matrix.dimension) + "," + str(
                self.matrix.dimension) + "!\" ]\n"

        # * NODES

        for fila in range(0, self.matrix.dimension):
            for columna in range(0, self.matrix.dimension):
                element = self.matrix.getElement(fila, columna)
                self.generateNode(element, str(fila), str(columna))

            self.generateRankAndReferences(str(fila))

        self.generateFinalReferences()
        self.dotStr += "}\n}"

    def generateNode(self, element, fila, columna):

        color = "blue"

        if not element:
            color = "red"

        body = "label=\"(" + fila + "," + columna + ")\", fillcolor=" + color + ", group=" + str(
            int(columna) + 1) + ", pos=\"" + fila + "," + columna + "!\" "
        self.dotStr += f"Columna{columna}Fila{fila}_{self.period}[{body}]\n"

    def generateRankAndReferences(self, fila):
        body = "rank=same;"

        for columna in range(0, self.matrix.dimension):
            body += f"Columna{str(columna)}Fila{fila}_{self.period}"

            if not columna == self.matrix.dimension:
                body += ";"

        self.dotStr += "{" + body + "}"

        references = ""
        for columna in range(0, self.matrix.dimension - 1):
            references += f"Columna{str(columna)}Fila{fila}_{self.period} -> Columna{str(columna+1)}Fila{fila}_{self.period} \n"
        self.dotStr += references

    def generateFinalReferences(self):
        references = ""
        for fila in range(0, self.matrix.dimension - 1):
            references += f"Columna0Fila{str(fila)}_{self.period} -> Columna0Fila{str(fila+1)}_{self.period} \n"
        self.dotStr += references