from controller.PatientRegister import PatientRegister
from data.doublyLinkedListWithIndex import DoublyLinkedListWithIndex
from data.matrix import SquareMatrix


def generateNextState(matrix):

    newMatrixState = SquareMatrix(matrix.dimension)

    for i in range(0, matrix.dimension):
        for j in range(0, matrix.dimension):

            infectedNeighboringCells = infectedNeighboringCellsCount(
                i, j, matrix)

            # Is infected
            # 1. Toda célula contagiada, continúa contagiada si tiene exactamente 2 o 3 células contagiadas en las celdas vecinas, de lo contrario sana para el siguiente periodo.
            if matrix.getElement(i, j):
                # if infectedNeighboringCells >= 2 or infectedNeighboringCells == 3:
                if infectedNeighboringCells == 2 or infectedNeighboringCells == 3:
                    newMatrixState.setElement(i, j, True)
                else:
                    newMatrixState.setElement(i, j, None)
            # Is healthy
            # 2. Cualquier célula sana que tenga exactamente 3 células contagiadas en las celdas vecinas, se contagia para el siguiente período.
            else:
                if infectedNeighboringCells == 3:
                    newMatrixState.setElement(i, j, True)
                else:
                    newMatrixState.setElement(i, j, None)

    return newMatrixState


def infectedNeighboringCellsCount(i, j, matrix):
    infectedCount = 0

    coords = {
        # Center
        "top": (i + 1, j),
        "bottom": (i - 1, j),
        "left": (i, j - 1),
        "right": (i, j + 1),
        # Diagonals
        "topLeft": (i - 1, j - 1),
        "topRight": (i - 1, j + 1),
        "bottomRight": (i + 1, j + 1),
        "bottomLeft": (i + 1, j - 1),
    }

    for coord in coords.values():
        if (coord[0] >= 0 and coord[0] < matrix.dimension) and (
                coord[1] >= 0 and coord[1] < matrix.dimension):
            if matrix.getElement(coord[0], coord[1]):
                infectedCount += 1

    return infectedCount
