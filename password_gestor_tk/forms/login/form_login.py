
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.Master.form_master import MasterPanel


class App:
    def verificar(self):
        if self.usuario.get() == "admin" and self.password.get() == "admin":
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(
                "Error", "Usuario o contraseña incorrectos", parent=self.ventana)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.configure(bg="#252525", width=700,
                               height=500, padx=10, pady=10, relief=tk.RIDGE)
        self.ventana.title("inicio de sesion")
        self.ventana.resizable(0, 0)

        utl.centrar_ventana(self.ventana, 700, 500)
        # logo
        logo = utl.leer_imagen("images/logo.png", (250, 250))
        # frame logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300,
                              relief=tk.SOLID, padx=10, pady=10, bg="#252525")
        frame_logo.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)
        # label logo
        label = tk.Label(frame_logo, image=logo, bg="#252525")
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame login
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg="#252525")
        frame_form.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
        frame_form_top = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg="#252525")
        frame_form_top.pack(side=tk.TOP, fill=tk.X)
        # fin del frame login
        title = tk.Label(frame_form_top, text="Inicio de Sesion", font=(
            "Storm Gust", 20), pady=20, bg="#252525", fg="#959595")
        title.pack(expand=tk.YES,)

        # _______Frame_fill_________________
        frame_form_fill = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg="#252525")
        frame_form_fill.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.BOTH)
        # ________etiqueta_usuario_____________________
        etiqueta_usuario = tk.Label(
            frame_form_fill, text="Usuario", font=("Storm Gust", 15), anchor="w", fg="white", border=4)
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=20)
        # ____Entry_Usuario____________________
        self.usuario = ttk.Entry(
            frame_form_fill, font=("Times", 18))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        # ________etiqueta_password_________
        etiqueta_password = tk.Label(
            frame_form_fill, text="Contraseña", font=("Storm Gust", 15), anchor="w", bg="#252525", fg="white")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=10)
        # ________Entry_password________________
        self.password = ttk.Entry(
            frame_form_fill, font=("Times", 18))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show=" ")
        # ________Boton_________________________
        login = tk.Button(frame_form_fill, text="Entrar", font=(
            "Storm Gust", 15), fg="white", bg="#707070", command=self.verificar)
        login.configure(width=20, activebackground="#707070")
        login.pack(fill=tk.X, padx=30, pady=20)
        # ________Registro_______________________
        registro = tk.Button(frame_form_fill, text="Registrarse", font=(
            "Storm Gust", 15), fg="white", bg="#707070", command="")
        registro.pack(fill=tk.X, padx=30, pady=20)
        self.ventana.mainloop()
