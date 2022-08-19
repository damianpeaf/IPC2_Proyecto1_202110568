from tkinter import *
from controller.Register import Register

from views.components.PatientsButtons import PatientsButtons


class ChoosePatient:

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("500x500")
        self.window.title("Selecciona el paciente")
        self.window.config(bg='#1B1F3B')
        self.initUI()

    def initUI(self):
        frame = Frame(self.window)

        for i in range(0, Register.patients.lenght):
            PatientsButtons(frame, self.window,
                            Register.patients.getElement(i))

        frame.pack(expand=1, fill="x")
        Button(self.window,
               text="Regresar",
               pady=5,
               padx=10,
               bg="#0D6EFD",
               fg="white",
               command=self.window.destroy).pack(expand=1, fill="x")
