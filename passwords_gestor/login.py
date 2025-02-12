# import os
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from password_management import MasterPanel
from roles import adminrol
from roles import userol


class LoginApp:
    def verify_user(self):
        user = self.entry_user.get()
        passwd = self.entry_password.get()

        # Verificar si el usuario y contraseña corresponden a un admin
        if adminrol.validate_admin_exists(user, passwd):
            self.show_welcome_message(user)
            print(user, "es administrador")
        return user

    """ elif userol.validate_user_exists(user, passwd):
            self.show_welcome_message(user)
            print(user, "es usuario normal")  # Agrega esta línea
            return user
            else:
                print("Error")
                print(user)"""

    def init_master_panel(self, user):
        # Si self.master_panel aún no está inicializado, inicialízalo
        if not hasattr(self, 'master_panel'):
            self.master_panel = None
        self.master_panel = MasterPanel(user)

    def show_welcome_message(self, user):
        welcome_label = ctk.CTkLabel(master=self.frame_login, text=f"Bienvenido {user}",
                                     font=("ButterCookie-Regular", 20), bg_color="#090e0c")
        welcome_label.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        def destroy_label():
            welcome_label.destroy()
            self.init_master_panel(user)
        self.ventana.after(3000, destroy_label)

    def __init__(self):
        self.ventana = ctk.CTk()
        self.master_panel = None
        self.ventana.title("inicio de sesion")
        self.ventana.geometry("500x300")
        self.ventana.resizable(0, 0)
        color = "#222221"
        self.frame_login = ctk.CTkFrame(
            master=self.ventana, fg_color=color)
        self.frame_login.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

        # frame del logo
        frame_logo = ctk.CTkFrame(
            master=self.frame_login, fg_color="#212023")
        frame_logo.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)

        # imagen

        # label del titulo
        label_title = ctk.CTkLabel(
            master=self.frame_login, text="Inicio de Sesion", fg_color=color, font=("ButterCookie-Regular", 20))
        label_title.pack(expand=tk.YES, fill=tk.BOTH)

        # frame principal de entrys
        frame_entry = ctk.CTkFrame(
            master=self.frame_login, fg_color=color)
        frame_entry.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        user_label = ctk.CTkLabel(
            master=frame_entry, text="Usuario:", font=("ButterCookie-Regular", 15), anchor="w", padx=30)
        user_label.pack(fill=tk.BOTH)

        self.entry_user = ctk.CTkEntry(
            master=frame_entry, placeholder_text="Usuario", )
        self.entry_user.pack(fill=tk.X, padx=30, pady=10)

        passwd_label = ctk.CTkLabel(
            master=frame_entry, text="Contraseña:", font=("ButterCookie-Regular", 15), anchor="w", padx=30)
        passwd_label.pack(fill=tk.BOTH)

        self.entry_password = ctk.CTkEntry(
            master=frame_entry, placeholder_text="Contraseña", show=" ")
        self.entry_password.pack(fill=tk.X, padx=30, pady=10)
        framebutton = ctk.CTkFrame(
            master=self.frame_login, fg_color=color)
        framebutton.pack(side=tk.BOTTOM, expand=tk.YES)
        login_button = ctk.CTkButton(master=framebutton, text="Iniciar sesion", fg_color="#212023", font=("ButterCookie-Regular", 20),
                                     command=self.verify_user)
        login_button.pack(side="left", padx=10, pady=10)
        register_button = ctk.CTkButton(master=framebutton, text="Registro", fg_color="#212023", font=("ButterCookie-Regular", 18),
                                        command=open_register)
        register_button.pack(side="left", padx=10, pady=10)
        self.ventana.mainloop()


def open_register():
    """_summary_"""
    new_window = ctk.CTk()
    new_window.geometry("250x250")
    new_window.resizable(False, False)
    new_window.title = "Registrar Usuario"
    user_label = ctk.CTkLabel(new_window, text="Usuario")
    user_label.pack()
    user_entry = ctk.CTkEntry(new_window, corner_radius=10)
    user_entry.pack()
    user_pass = ctk.CTkLabel(new_window, text="Contraseña")
    user_pass.pack()
    pass_entry = ctk.CTkEntry(new_window, show="*", corner_radius=10)
    pass_entry.pack()
    register_label = ctk.CTkLabel(new_window, text="", font=("Arial", 16))
    register_label.pack()

    # Añadimos el botón de registro y le pasamos las entradas como argumentos
    admin_checkbox_var = tk.BooleanVar()
    user_checkbox_var = tk.BooleanVar()

    def on_register(window, user_entry, pass_entry):
        if admin_checkbox_var.get():
            adminrol.on_register(window, user_entry, pass_entry)
        elif user_checkbox_var.get():
            userol.on_register(window, user_entry, pass_entry)

    register_button = ctk.CTkButton(
        new_window, text="Registrarse",
        command=lambda: on_register(new_window, user_entry, pass_entry))

    register_button.pack()
    checkbox_frame = ctk.CTkFrame(new_window)
    checkbox_frame.pack(anchor="w", padx=10, pady=10)

    # Checkboxes para Admin y User dentro del mismo Frame
    admin_checkbox = ctk.CTkCheckBox(
        checkbox_frame, text="Admin", variable=admin_checkbox_var)
    admin_checkbox.pack(side="left", padx=10, pady=10)

    user_checkbox = ctk.CTkCheckBox(
        checkbox_frame, text="User", variable=user_checkbox_var)
    user_checkbox.pack(side="left", padx=10, pady=10)
    new_window.mainloop()


LoginApp()
