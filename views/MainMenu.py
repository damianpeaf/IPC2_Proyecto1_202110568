from tkinter import *
from views.ChooseFile import ChooseFile
from views.ChoosePatient import ChoosePatient


class MainMenu:

    masterWindow = Tk()

    def __init__(self):
        self.masterWindow.geometry("400x350")
        self.masterWindow.title("Menú de inicio")
        self.masterWindow.config(bg='#1B1F3B')
        self.initUI()
        self.masterWindow.mainloop()

    def goToChooseFile(self):
        newWindow = ChooseFile(self.masterWindow)
        newWindow.window.grab_set()

    def goToChoosePatient(self):
        newWindow = ChoosePatient(self.masterWindow)
        newWindow.window.grab_set()

    def initUI(self):

        titleFont = ("Helvetica", 12, "bold")
        buttonFont = ("Helvetica", 10, "bold")

        # Información
        Label(self.masterWindow,
              text="Proyceto 1 IPC2",
              pady=5,
              font=titleFont,
              bg='#1B1F3B',
              fg='white').pack()
        Label(self.masterWindow,
              text="Nombre: Damián Ignacio Peña Afre",
              pady=5,
              bg='#1B1F3B',
              fg='white').pack()

        Label(self.masterWindow,
              text="Carné: 202110568",
              pady=5,
              bg='#1B1F3B',
              fg='white').pack()

        # Separador
        Label(self.masterWindow,
              text="Opciones:",
              pady=5,
              font=titleFont,
              bg='#1B1F3B',
              fg='white').pack()

        # Boton
        Button(self.masterWindow,
               text="Cargar archivo",
               pady=5,
               padx=10,
               bg="#0D6EFD",
               fg="white",
               font=buttonFont,
               command=self.goToChooseFile).pack(expand=1, fill="x")

        # Boton
        Button(self.masterWindow,
               text="Simulaciones",
               pady=5,
               padx=10,
               bg="#0D6EFD",
               fg="white",
               font=buttonFont,
               command=self.goToChoosePatient).pack(expand=1, fill="x")
