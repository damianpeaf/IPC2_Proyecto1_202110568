from os import system


class GraphvizMatrixParser():

    def __init__(self, history, name):
        self.history = history
        self.name = name
        self.parseToSrtDot()
        self.generateFile()

    def generateFile(self):
        try:
            f = open(f"./dot/historial{self.name}.dot", "x")
            f.write(self.dotStr)
            f.close()

            print('Archivo dot generado')

            return True

        except Exception as e:
            print(e)
            return False

    def parseToSrtDot(self):

        self.dotStr = ""

        # * Init
        self.dotStr += f"digraph P{str(self.name)}" + "{\n"
        self.dotStr += "node [shape=box, nodesep=1, fillcolor=blue, style=filled]\n"
        self.dotStr += "compound=true\n"
        self.dotStr += "edge[dir=\"both\"]\n"

        for i in range(0, self.history.lenght):

            matrix = self.history.getElement(i)
            period = str(i)

            self.dotStr += "subgraph cluster_periodo" + period + " {\n"
            self.dotStr += "Label_" + period + \
                "[label = \"periodo " + period + " \", style=rounded ]\n"

            # * NODES

            for fila in range(0, matrix.dimension):
                for columna in range(0, matrix.dimension):
                    element = matrix.getElement(fila, columna)
                    self.generateNode(element, str(fila), str(columna), period)

                self.generateRankAndReferences(str(fila), period, matrix)

            self.generateFinalReferences(period, matrix)

            self.dotStr += "}\n"

        self.dotStr += "}"

    def generateNode(self, element, fila, columna, period):

        color = "red"

        if not element:
            color = "blue"

        body = "label=\"(" + fila + "," + columna + ")\", fillcolor=" + color + ", group=" + str(
            int(columna) + 1) + " "
        self.dotStr += f"Columna{columna}Fila{fila}_{period}[{body}]\n"

    def generateRankAndReferences(self, fila, period, matrix):
        body = "rank=same;"

        for columna in range(0, matrix.dimension):
            body += f"Columna{str(columna)}Fila{fila}_{period}"

            if not columna == matrix.dimension:
                body += ";"

        self.dotStr += "{" + body + "}"

        references = ""
        for columna in range(0, matrix.dimension - 1):
            references += f"Columna{str(columna)}Fila{fila}_{period} -> Columna{str(columna+1)}Fila{fila}_{period} \n"
        self.dotStr += references

    def generateFinalReferences(self, period, matrix):
        references = ""
        for fila in range(0, matrix.dimension - 1):
            references += f"Columna0Fila{str(fila)}_{period} -> Columna0Fila{str(fila+1)}_{period} \n"
        self.dotStr += references
