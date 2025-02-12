"""importar librerias"""
from tkinter import messagebox
import os
import sqlite3
import customtkinter as ctk


BD = "data/passwords.db"


def create_default_user():
    if validate_user_exists("admin", "password123"):
        bdd = sqlite3.connect(BD)
        cursor = bdd.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND password=?",
                       ("admin", "password123"))
        resultado = cursor.fetchone()
        bdd.close()
        print("El usuario por defecto ya existe.")

        return resultado is not None
    else:
        create_db("admin", "password123")
        print("Usuario por defecto creado con éxito.")


def register():
    """_summary_"""
    app = ctk.CTk()
    app.geometry("220x200")
    app.resizable(False, False)

    user_label = ctk.CTkLabel(app, text="Usuario")
    user_label.pack()
    user_entry = ctk.CTkEntry(app, corner_radius=10)
    user_entry.pack()
    user_pass = ctk.CTkLabel(app, text="Contraseña")
    user_pass.pack()
    pass_entry = ctk.CTkEntry(app, show="*", corner_radius=10)
    pass_entry.pack()
    register_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
    register_label.pack()

    # Añadimos el botón de registro y le pasamos las entradas como argumentos
    register_button = ctk.CTkButton(
        app, text="Registrarse", command=lambda: [on_register(app, user_entry, pass_entry)], corner_radius=10)
    register_button.pack()
    create_default_user()
    app.mainloop()


def validate_user_exists(nombre, password):
    bdd = sqlite3.connect(BD)
    cursor = bdd.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND password=?",
                   (nombre, password))
    resultado = cursor.fetchone()
    bdd.close()

    return resultado is not None


def on_register(app, user_entry, pass_entry):
    nombre = user_entry.get()
    password = pass_entry.get()

    # Verifica si el usuario ya existe
    if validate_user_exists(nombre, password):
        messagebox.showerror("Error", "El usuario y la clave ya existen")
        messagebox.showinfo(
            "Error", "el usuario admin por defecto ya existe, por seguridad debe borrarlo")
    else:
        create_db(nombre, password)
        messagebox.showinfo("Éxito", "Registrado con éxito")
        app.destroy()

# El resto del código permanece igual...


def conectdb():
    """_summary_
    Conect the database to the program
    Returns:
        _type_: _description_
    """
    sqlite3.connect("data/passwords.db")
    return "data/passwords.db"


def create_db(nombre, password):
    route = conectdb()
    if os.path.exists(route):
        bdd = sqlite3.connect(route)
        cursor = bdd.cursor()
        create_table_query1 = '''
            CREATE TABLE if not exists usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                password varchar(255)
            )'''

        create_table_query2 = '''
            CREATE TABLE if not exists Cuentas (
                id INTEGER PRIMARY KEY,
                Cuenta TEXT,
                usuario TEXT,
                password varchar(255)
            )'''
        cursor.execute(create_table_query1)
        cursor.execute(create_table_query2)
        insert_user_query1 = "INSERT INTO usuarios (nombre, password) VALUES (?,?)"
        cursor.execute(insert_user_query1, (nombre, password))
        bdd.commit()
        bdd.close()

    else:
        bdd = sqlite3.connect(route)
        cursor = bdd.cursor()

        create_table_query1 = '''
            CREATE TABLE if not exists usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                password varchar(255)
            )'''

        create_table_query2 = '''
            CREATE TABLE if not exists Cuentas (
                id INTEGER PRIMARY KEY,
                Cuenta TEXT,
                usuario TEXT,
                password varchar(255)
            )'''

        cursor.execute(create_table_query1)
        cursor.execute(create_table_query2)

        insert_user_query1 = "INSERT INTO usuarios (nombre, password) VALUES (?, ?)"
        cursor.execute(insert_user_query1, (nombre, password))

        bdd.commit()
        bdd.close()


def read():
    pass


def update():
    pass


def delete():
    pass


create_db("admin", "password123")
# crear una funcion de conexion a la base de datos e instanciarla en el registro y la creacion de la base de datos
# tambien crear un crud para crear,leer,actualizar y borrar cada uno en una funcion para luego ser llamada desde el pasword manager
