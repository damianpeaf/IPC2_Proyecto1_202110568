from tkinter import *

from controller.Register import Register
from views.CellViewSimulation import CellViewSimulation


class PatientsButtons():

    def __init__(self, frame, window):
        for i in range(0, Register.patients.lenght):
            register = Register.patients.getElement(i)
            Button(frame,
                   text=register.name,
                   pady=5,
                   padx=10,
                   bg="#454ADE",
                   fg="white",
                   command=lambda: CellViewSimulation(window, register)).pack(
                       expand=1, fill="x")
