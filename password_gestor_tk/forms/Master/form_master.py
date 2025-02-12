import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl


class MasterPanel:
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.title("Password Manager")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="white")
        self.ventana.resizable(0, 0)

        logo = utl.leer_imagen("images/logo.png", (250, 250))
        label = tk.Label(self.ventana, image=logo, bg="white")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        self.ventana.mainloop()
