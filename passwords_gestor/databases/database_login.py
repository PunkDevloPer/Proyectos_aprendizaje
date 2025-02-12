"""importar librerias"""
import os
import sqlite3


def database_login():
    """Conecta la base de datos al programa."""
    conexion = sqlite3.connect("data/login.db")
    return conexion


def createdb():
    """crea la base de datos"""
    conexion = database_login()
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        password TEXT NOT NULL,
        rol TEXT)''')  # Corregimos la definición de las columnas
    cursor.execute('''CREATE TABLE IF NOT EXISTS admins(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        password TEXT NOT NULL,
        rol TEXT)''')
    conexion.commit()
    conexion.close()


def create_admin(nombre, password):
    """create database if not exist"""
    if os.path.exists("data/login.db"):
        bdd = sqlite3.connect('data/login.db')
        cursor = bdd.cursor()
        insert_user_query1 = "INSERT INTO admins (nombre, password,rol) VALUES (?, ?,'admin')"
        cursor.execute(insert_user_query1, (nombre, password))
        bdd.commit()
        bdd.close()


def create_user(nombre, password):
    """create database if not exist"""
    if os.path.exists("data/login.db"):
        bdd = sqlite3.connect('data/login.db')
        cursor = bdd.cursor()
        insert_user_query1 = "INSERT INTO users (nombre, password,rol) VALUES (?, ?,'user')"
        cursor.execute(insert_user_query1, (nombre, password))
        bdd.commit()
        bdd.close()


def read():
    """read the database"""
    pass


def update():
    """update the database"""
    pass


def delete():
    """delete user in the database"""
    pass
