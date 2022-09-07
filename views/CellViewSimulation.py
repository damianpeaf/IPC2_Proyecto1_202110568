import threading
import time
from tkinter import *
from tkinter import messagebox
from controller.Register import Register
from controller.Report import Report
from controller.Simulation import Simulation

from views.components.CellBoard import CellBoard
from views.components.SimulationInfoLabels import SimulationInfoLabels


class CellViewSimulation:

    def __init__(self, parent, patientRegister):
        self.simulation = Simulation(patientRegister)
        self.patientRegister = patientRegister
        self.window = Toplevel(parent)
        self.window.geometry("800x480")
        self.window.title(f"Simulación {patientRegister.name}")
        self.window.config(bg='#1B1F3B')
        self.initUI()

    def refreshInfo(self):

        self.info = self.simulation.info()
        self.actualMatrix = self.simulation.actualState

        self.infoFrame = Frame(self.window, bg='#1B1F3B')
        SimulationInfoLabels(self.infoFrame, self.info)
        self.infoFrame.pack()

        self.boardFrame = Frame(self.window, bg='#1B1F3B')

        CellBoard(self.boardFrame, self.actualMatrix)
        self.boardFrame.pack()

    def prevState(self):
        self.simulation.prevState()
        self.infoFrame.destroy()
        self.boardFrame.destroy()
        self.refreshInfo()

    def nextState(self):
        self.simulation.nextState()
        self.infoFrame.destroy()
        self.boardFrame.destroy()
        self.refreshInfo()

        if self.simulation.simulationEnd:
            messagebox.showinfo(title="Aviso", message='Simulacion terminada')

    def untilFindDisease(self):
        self.simulation.runAllStates()
        self.infoFrame.pack_forget()
        self.boardFrame.pack_forget()
        self.refreshInfo()
        messagebox.showinfo(title="Aviso", message='Simulacion terminada')

    def autoSimulateStart(self):
        self.simulationButtonStart['state'] = DISABLED
        self.simulationButtonEnd['state'] = NORMAL
        self.threadContinue = True

        self.simulationThread = threading.Thread(target=self.autoSimulate)
        self.simulationThread.start()

    def autoSimulate(self):
        while not self.simulation.simulationEnd:
            time.sleep(0.5)
            self.nextState()

            if not self.threadContinue:
                break

    def autoSimulateStop(self):
        self.threadContinue = FALSE
        self.simulationButtonStart['state'] = NORMAL
        self.simulationButtonEnd['state'] = DISABLED

    def generateIndividualReport(self):
        res = Report.generateIndividualReport(self.patientRegister)

        if res:
            messagebox.showinfo(title="Aviso", message='Reporte Generado')
        else:
            messagebox.showerror(
                title="Error", message='Hubo un error en la generación')

    def initUI(self):

        # * Buttons
        self.buttonFrame = Frame(self.window, bg='#1B1F3B')
        Button(self.buttonFrame,
               text="regresar",
               pady=5,
               padx=10,
               bg="#DC2656",
               fg="white",
               command=self.window.destroy).grid(row=0, column=0)

        self.simulationButtonStart = Button(self.buttonFrame,
                                            text="Auto simular",
                                            pady=5,
                                            padx=10,
                                            bg="#4B1C7D",
                                            fg="white",
                                            command=self.autoSimulateStart,
                                            state=NORMAL)
        self.simulationButtonStart.grid(row=0, column=1, sticky=N + S + E + W)

        self.simulationButtonEnd = Button(self.buttonFrame,
                                          text="Detener simulacion",
                                          pady=5,
                                          padx=10,
                                          bg="#4B1C7D",
                                          fg="white",
                                          command=self.autoSimulateStop,
                                          state=DISABLED)
        self.simulationButtonEnd.grid(row=0, column=2, sticky=N + S + E + W)

        Button(self.buttonFrame,
               text="Anterior periodo",
               pady=5,
               padx=10,
               bg="#454ADE",
               fg="white",
               command=self.prevState).grid(row=0,
                                            column=3,
                                            sticky=N + S + E + W)

        Button(self.buttonFrame,
               text="Siguiente periodo",
               pady=5,
               padx=10,
               bg="#454ADE",
               fg="white",
               command=self.nextState).grid(row=0,
                                            column=4,
                                            sticky=N + S + E + W)

        Button(self.buttonFrame,
               text="Simular todo",
               pady=5,
               padx=10,
               bg="#1A9A67",
               fg="white",
               command=self.untilFindDisease).grid(row=0,
                                                   column=5,
                                                   sticky=N + S + E + W)

        Button(self.buttonFrame,
               text="Reporte Individual",
               pady=5,
               padx=10,
               bg="#DC2656",
               fg="white",
               command=self.generateIndividualReport).grid(row=0,
                                                           column=6,
                                                           sticky=N + S + E + W)

        self.buttonFrame.grid_columnconfigure(0, weight=1)
        self.buttonFrame.pack(expand=1, fill="x")

        # * End buttons

        self.refreshInfo()
