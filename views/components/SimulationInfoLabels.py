from tkinter import *


class SimulationInfoLabels():

    def __init__(self, frame, info):
        Label(frame, text=info["diseases"], bg='#1B1F3B', fg="white").pack()
        Label(frame, text=info["stats"], bg='#1B1F3B', fg="white").pack()
        Label(frame, text=info["patient"], bg='#1B1F3B', fg="white").pack()
