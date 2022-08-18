from tkinter import *


class MainMenu:

    masterWindow = Tk()

    def __init__(self):
        self.masterWindow.geometry("400x350")
        self.masterWindow.title("Menú de inicio")
        self.initUI()
        self.masterWindow.mainloop()

    def initUI(self):

        titleFont = ("Helvetica", 12, "bold")
        buttonFont = ("Helvetica", 10, "bold")

        # Información
        Label(
            self.masterWindow,
            text="IPC2",
            pady=5,
            font=titleFont,
        ).grid(row=0, column=0, pady=10)
        Label(self.masterWindow,
              text="Nombre: Damián Ignacio Peña Afre",
              pady=5).grid(row=1, column=0, pady=5)
        Label(self.masterWindow, text="Carné: 202110568",
              pady=5).grid(row=2, column=0, pady=5)

        # Separador
        Label(self.masterWindow, text="Opciones:", pady=5,
              font=titleFont).grid(row=3, column=0, pady=5)
