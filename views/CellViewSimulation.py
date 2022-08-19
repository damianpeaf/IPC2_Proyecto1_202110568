from tkinter import *
from controller.Register import Register
from controller.Simulation import Simulation

from views.components.CellBoard import CellBoard
from views.components.SimulationInfoLabels import SimulationInfoLabels


class CellViewSimulation:

    def __init__(self, parent, patientRegister):
        self.simulation = Simulation(patientRegister)
        self.window = Toplevel(parent)
        self.window.geometry("800x480")
        self.window.title(f"Simulación {patientRegister.name}")
        self.initUI()

    def refreshInfo(self):

        self.info = self.simulation.info()
        self.actualMatrix = self.simulation.actualState
        self.infoFrame = Frame(self.window)
        SimulationInfoLabels(self.infoFrame, self.info)
        self.infoFrame.pack()

        self.boardFrame = Frame(self.window)
        CellBoard(self.boardFrame, self.actualMatrix)
        self.boardFrame.pack()

    def nextState(self):
        self.simulation.nextState()
        self.infoFrame.pack_forget()
        self.boardFrame.pack_forget()
        self.refreshInfo()

    def initUI(self):

        # * Buttons
        buttonFrame = Frame(self.window)
        Button(buttonFrame,
               text="regresar",
               pady=5,
               padx=10,
               bg="#DC2656",
               fg="white",
               command=self.window.destroy).grid(row=0, column=0)

        Button(buttonFrame,
               text="Generar XML",
               pady=5,
               padx=10,
               bg="#1A9A67",
               fg="white").grid(row=0, column=3, sticky=N + S + E + W)

        Button(buttonFrame,
               text="Correr toda la simulacion",
               pady=5,
               padx=10,
               bg="#4B1C7D",
               fg="white").grid(row=0, column=1, sticky=N + S + E + W)

        Button(buttonFrame,
               text="Adelantar un periodo",
               pady=5,
               padx=10,
               bg="#454ADE",
               fg="white",
               command=self.nextState).grid(row=0,
                                            column=2,
                                            sticky=N + S + E + W)

        buttonFrame.grid_columnconfigure(0, weight=1)
        buttonFrame.pack(expand=1, fill="x")

        # * End buttons

        self.refreshInfo()
