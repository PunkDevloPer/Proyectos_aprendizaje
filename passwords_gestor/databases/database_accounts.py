import sqlite3


def database_user_account():
    """Conecta la base de datos al programa."""
    conexion = sqlite3.connect("data/accounts.db")
    return conexion


def createdb():
    """crea la base de datos"""
    conexion = database_user_account()
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts(
        id INTEGER PRIMARY KEY,
        nombre de usuario TEXT NOT NULL,
        cuenta TEXT NOT NULL,
        contraseña TEXT NOT NULL)''')
    conexion.commit()
    conexion.close()


def read():
    """read the database"""
    pass


def update():
    """update the database"""
    pass


def delete():
    """delete user in the database"""
    pass
