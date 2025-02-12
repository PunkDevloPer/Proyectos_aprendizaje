  # Crear una nueva ventana principal personalizada
    self.ventana.title("Gestor de Contraseñas")
    self.ventana.geometry("400x500")
    self.ventana.resizable(False, False)

    # Crear Entry para la cuenta
    label_cuenta = ctk.CTkLabel(master=root_tk, text="Cuenta:")
    label_cuenta.pack(pady=5)
    entry_cuenta = ctk.CTkEntry(master=root_tk)
    entry_cuenta.pack(pady=5)

    # Crear Entry para el usuario/correo
    label_usuario = ctk.CTkLabel(master=root_tk, text="Usuario/Correo:")
    label_usuario.pack(pady=5)
    entry_usuario = ctk.CTkEntry(master=root_tk)
    entry_usuario.pack(pady=5)

    # Crear Entry para la contraseña
    label_contrasena = ctk.CTkLabel(master=root_tk, text="Contraseña:")
    label_contrasena.pack(pady=5)
    # Mostrar asteriscos para ocultar la contraseña
    entry_contrasena = ctk.CTkEntry(master=root_tk, show="*")
    entry_contrasena.pack(pady=5)
    # Botón de cierre
    boton_cerrar = ctk.CTkButton(
        master=root_tk, text="Cerrar", command=root_tk.destroy, width=10, height=10, corner_radius=10)
    boton_cerrar.pack(pady=10)
    root_tk.mainloop()


def verify_user(user_entry, pass_entry):
    usuario = user_entry.get()
    password = pass_entry.get()
    bd = sqlite3.connect("data/passwords.db")
    cursors = bd.cursor()
    username = usuario
    cursors.execute(
        'SELECT * FROM usuarios WHERE nombre = ? AND password = ?', (username, password))
    results = cursors.fetchall()
    bd.close()

    # Verificar si el usuario existe
    for resultado in results:
        if resultado[1] == username and resultado[2] == password:
            MasterPanel()
            break
        elif resultado[2] != password:
            print('La contraseña es incorrecta.')
            break
        else:
            print(f'El usuario {username} no existe en la base de datos.')