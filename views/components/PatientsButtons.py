from tkinter import *

from controller.Register import Register
from views.CellViewSimulation import CellViewSimulation


class PatientsButtons():

    def __init__(self, frame, window, patientRegister):
        Button(
            frame,
            text=patientRegister.name,
            pady=5,
            padx=10,
            bg="#454ADE",
            fg="white",
            command=lambda: CellViewSimulation(window, patientRegister)).pack(
                expand=1, fill="x")
