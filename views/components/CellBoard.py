from tkinter import *


class CellBoard():

    def __init__(self, frame, matrix):
        if matrix:
            for i in range(0, matrix.dimension):
                for j in range(0, matrix.dimension):
                    content = matrix.getElement(i, j)
                    label = Label(frame, text=" " * 10)

                    if content:
                        label.config(bg="red")
                    else:
                        label.config(bg="blue")

                    label.grid(row=i, column=j, padx=1, pady=1)
        else:
            return