import os
import customtkinter as ctk
import tkinter as tk
from PIL import Image
import database
from password_management import MasterPanel as pswd


class App():
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.config(bg="black")
        self.ventana.title("inicio de sesion")
        self.ventana.geometry("500x300")
        self.ventana.resizable(0, 0)

        self.frame_login = ctk.CTkFrame(
            master=self.ventana, fg_color="#071A1F")
        self.frame_login.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

        # frame del logo
        frame_logo = ctk.CTkFrame(
            master=self.frame_login, fg_color="#132043")
        frame_logo.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)

        # imagen
        my_logo = ctk.CTkImage(light_image=Image.open(
            "images/logn.png"), size=(190, 190))

        # label_logo
        label_logo = ctk.CTkLabel(
            master=frame_logo, image=my_logo, text="", width=200, height=200)
        label_logo.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        # label del titulo
        label_title = ctk.CTkLabel(
            master=self.frame_login, text="Inicio de Sesion", font=("atrial", 25))
        label_title.pack(expand=tk.YES, fill=tk.BOTH)

        # frame principal de entrys
        frame_entry = ctk.CTkFrame(
            master=self.frame_login, fg_color="#071A1F")
        frame_entry.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        user_label = ctk.CTkLabel(
            master=frame_entry, text="Usuario", font=("arial", 25))
        user_label.pack(fill=tk.X, padx=20, pady=10)

        self.entry_user = ctk.CTkEntry(
            master=frame_entry, placeholder_text="Usuario", fg_color="#F0FAF8")
        self.entry_user.pack(fill=tk.X, padx=20, pady=10)

        passwd_label = ctk.CTkLabel(
            master=frame_entry, text="Contraseña", font=("arial", 25))
        passwd_label.pack(fill=tk.X, padx=20, pady=10)

        self.entry_password = ctk.CTkEntry(
            master=frame_entry, placeholder_text="Contraseña", show="*", fg_color="#F0FAF8")
        self.entry_password.pack(fill=tk.X, padx=20, pady=10)

        login_button = ctk.CTkButton(master=self.frame_login, text="Iniciar sesion",
                                     command=self.verificar_login, width=10, height=10, corner_radius=10)
        login_button.pack()
        self.ventana.mainloop()

    def verificar_login(self):
        user = self.entry_user.get()
        passwd = self.entry_password.get()
        print(user, passwd)
        if database.validate_user_exists(user, passwd):
            self.ventana.iconify()
            welcome = ctk.CTkLabel(
                master=pswd(), text="¡Bienvenido " + user + "!")
            welcome.pack(pady=10, padx=10, fill=tk.BOTH, expand=tk.YES)


App()
