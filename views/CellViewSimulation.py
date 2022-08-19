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
        self.refreshInfo()
        self.initUI()

    def refreshInfo(self):
        self.info = self.simulation.info()
        self.actualMatrix = self.simulation.actualState

    def initUI(self):

        infoFrame = Frame(self.window)
        SimulationInfoLabels(infoFrame, self.info)
        infoFrame.pack()

        boardFrame = Frame(self.window)
        CellBoard(boardFrame, self.actualMatrix)
        boardFrame.pack()

        buttonFrame = Frame(self.window)
        Button(buttonFrame,
               text="regresar",
               pady=5,
               padx=10,
               bg="#DC2656",
               fg="white",
               command=self.window.destroy).grid(row=0,
                                                 column=0,
                                                 sticky=N + S + E + W)

        Button(buttonFrame,
               text="Correr toda la simulacion",
               pady=5,
               padx=10,
               bg="#4B1C7D",
               fg="white",
               command=self.window.destroy).grid(row=0,
                                                 column=1,
                                                 sticky=N + S + E + W)

        Button(buttonFrame,
               text="Adelantar un periodo",
               pady=5,
               padx=10,
               bg="#454ADE",
               fg="white",
               command=self.window.destroy).grid(row=0,
                                                 column=2,
                                                 sticky=N + S + E + W)

        buttonFrame.grid_columnconfigure(0, weight=1)
        buttonFrame.pack(expand=1, fill="x")
