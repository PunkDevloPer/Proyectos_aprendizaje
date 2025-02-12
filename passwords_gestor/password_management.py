"""password manager"""
import customtkinter as ctk
import sqlite3
from roles import adminrol, userol
from databases import database_accounts as dtb_accounts


class MasterPanel:
    """Clase del panel principal del gestor de contraseñas"""

    def __init__(self, user):
        self.user = user
        self.ventana = ctk.CTk()
        self.ventana.geometry("500x500")
        self.ventana.resizable(0, 0)
        self.ventana.title("Gestor de Contraseñas")
        self.setup_window()
        self.data_counts()

    def setup_window(self):
        frame = ctk.CTkFrame(master=self.ventana)
        frame.configure(width=500, height=500)
        frame.pack(side="left", fill="both")
        frame_img = ctk.CTkFrame(
            master=frame, width=100, height=100, corner_radius=100)
        frame_img.pack(anchor="center", padx=10, pady=10)
        label_nick = ctk.CTkLabel(master=frame, text=f"Usuario : {self.user}",
                                  font=("ButterCookie-Regular", 20))
        label_nick.pack(anchor="nw", padx=10, pady=10,)

        boton_accounts = ctk.CTkButton(master=frame, text="Cuentas",
                                       command=self.data_counts)
        boton_accounts.pack(anchor="w", padx=10, pady=10)

        if adminrol.validate_admin_exists(self.user, ""):
            print("es admin")
            botton_add = ctk.CTkButton(
                master=frame, text="Anadir admin", command=adminrol.open_register_admin)
            botton_add.pack(anchor="w", padx=10, pady=10)

            config = ctk.CTkButton(master=frame, text="Configuracion")
            config.pack(anchor="w", padx=10, pady=10)
        else:

            add_user = ctk.CTkButton(
                master=frame, text="Anadir Cuentas", command=dtb_accounts.createdb)
            add_user.pack(anchor="w", padx=10, pady=10)
            exportdb = ctk.CTkButton(
                master=frame, text="Exportar Base de datos")
            exportdb.pack(anchor="w", padx=10, pady=10)

        self.ventana.mainloop()

    def data_counts(self):
        conn = sqlite3.connect('data/login.db')
        cursor = conn.cursor()

        # Obtener los datos de la tabla usuarios
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()

        # Crear un Frame para mostrar los datos dentro de la ventana principal
        data_frame = ctk.CTkFrame(self.ventana)
        data_frame.pack(side="right", fill="both", expand=True)

        # Mostrar los datos en el Frame
        for row_index, row_data in enumerate(data):
            for col_index, cell_value in enumerate(row_data):
                # Crear etiquetas para mostrar los datos en el Frame
                label = ctk.CTkLabel(data_frame, text=str(cell_value))
                label.grid(row=row_index, column=col_index, padx=5, pady=5)

        # Cerrar la conexión a la base de datos
        conn.close()
