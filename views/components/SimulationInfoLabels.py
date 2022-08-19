from tkinter import *


class SimulationInfoLabels():

    def __init__(self, frame, info):
        Label(frame, text=info["diseases"]).pack()
        Label(frame, text=info["stats"]).pack()
        Label(frame, text=info["patient"]).pack()