import sqlite3
import os
from databases import database_login as dtblogn


def open_register_admin():
    """
    Purpose: 
    """
    dtblogn.createdb()


def validate_admin_exists(nombre, password):
    """Validate is user exists in database"""
    bdd = sqlite3.connect('data/login.db')
    cursor = bdd.cursor()
    create_table_users = '''
            CREATE TABLE if not exists admins (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                password varchar(255),
                rol TEXT
            )'''
    cursor.execute(create_table_users)
    cursor.execute("SELECT * FROM admins WHERE nombre=? AND password=? AND rol='admin'",
                   (nombre, password))
    resultado = cursor.fetchone()
    bdd.close()
    print(resultado)
    return resultado is not None


def on_register(app, user_entry, pass_entry):
    """Register user function"""
    nombre = user_entry.get()
    password = pass_entry.get()

    # Verifica si el usuario ya existe
    if validate_admin_exists(nombre, password):
        print("Error", "El usuario y la clave ya existen")

    else:
        open_register_admin()
        dtblogn.create_admin(nombre, password)
