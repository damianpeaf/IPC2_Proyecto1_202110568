from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from controller.Register import Register


class ChooseFile():

    window = None

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("700x110")
        self.window.title("Sekeccuibar archivo")
        self.window.config(bg='#1B1F3B')
        self.initUI()

    def launchFileExplorer(self):
        path = filedialog.askopenfilename(initialdir="./",
                                          title="Seleccionar achivo",
                                          filetypes=[("XML Files", "*.xml")])

        self.entryPath.delete(0, END)
        self.entryPath.insert(0, path)

    def loadFile(self):
        path = self.entryPath.get()

        response = Register.loadData(path)
        if response["ok"]:
            messagebox.showinfo(title="Aviso", message=response["msg"])
        else:
            messagebox.showerror(title="Error", message=response["msg"])

    def initUI(self):

        textFont = ("Helvetica", 14, "bold")
        buttonFont = ("Helvetica", 12, "bold")

        Label(self.window,
              text="Ruta: ",
              font=textFont,
              bg='#1B1F3B',
              fg="white").grid(row=0, column=0)

        self.entryPath = Entry(self.window, width=80)
        self.entryPath.grid(row=0, column=1)

        Button(self.window,
               font=buttonFont,
               text="Cargar",
               pady=5,
               padx=10,
               bg="#198754",
               command=self.loadFile).grid(row=1, column=0, padx=5)

        Button(self.window,
               font=buttonFont,
               text="Abrir Explorador",
               pady=5,
               padx=10,
               bg="#0DCAF0",
               command=self.launchFileExplorer).grid(row=1, column=1, padx=5)

        Button(self.window,
               font=buttonFont,
               text="Regresar",
               pady=5,
               padx=10,
               bg="#0D6EFD",
               command=self.window.destroy).grid(row=1, column=2, padx=5)
