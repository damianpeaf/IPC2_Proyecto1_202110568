from tkinter import *
from tkinter import messagebox
from controller.Register import Register
from controller.Report import Report

from views.components.PatientsButtons import PatientsButtons


class ChoosePatient:

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("500x500")
        self.window.title("Selecciona el paciente")
        self.window.config(bg='#1B1F3B')
        self.initUI()

    def handleCleanData(self):
        Register.cleanRegisters()
        self.window.destroy()

    def handleGenerateReports(self):
        response = Report.generateAllReports(Register.patients)

        if response:
            messagebox.showinfo(title="Aviso", message='Reporte Generado')
        else:
            messagebox.showerror(title="Error",
                                 message='Error al generar el reporte')

    def initUI(self):
        frame = Frame(self.window, bg='#1B1F3B')

        if Register.patients.lenght == 0:
            Label(frame,
                  text=" No hay pacientes cargados",
                  bg='#1B1F3B',
                  fg="white").pack()
        else:
            for i in range(0, Register.patients.lenght):
                PatientsButtons(frame, self.window,
                                Register.patients.getElement(i))

        frame.pack(expand=1, fill="x")

        Button(self.window,
               text="Borrar datos cargados",
               pady=5,
               padx=10,
               bg="#DC2656",
               fg="white",
               command=self.handleCleanData).pack(expand=1, fill="x")

        Button(self.window,
               text="Generar informe",
               pady=5,
               padx=10,
               bg="#4B1C7D",
               fg="white",
               command=self.handleGenerateReports).pack(expand=1, fill="x")

        Button(self.window,
               text="Regresar",
               pady=5,
               padx=10,
               bg="#0D6EFD",
               fg="white",
               command=self.window.destroy).pack(expand=1, fill="x")
