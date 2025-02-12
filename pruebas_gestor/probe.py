
class Root(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x350")
        self.resizable(False, False)
        login_image = ctk.CTkImage(light_image=Image.open("images/logn.png"),
                                   size=(90, 90))

        ctk.CTkLabel(self, image=login_image, text="").pack()

        user_label = ctk.CTkLabel(
            self, text="Usuario", font=("Arial", 16), height=30)
        user_label.pack()
        self.user_entry = ctk.CTkEntry(
            self, height=40, width=250, corner_radius=10)
        self.user_entry.pack()

        user_pass = ctk.CTkLabel(
            self, text="Contraseña", font=("Arial", 16), height=30)
        user_pass.pack()
        self.pass_entry = ctk.CTkEntry(
            self, show="*", height=40, width=250, corner_radius=10)
        self.pass_entry.pack()

        user_separator = ctk.CTkLabel(self, text="")
        user_separator.pack()

        login_button = ctk.CTkButton(
            master=self, text="Entrar", command=self.verificar_login, corner_radius=10)
        login_button.pack()

        register_label = ctk.CTkLabel(
            self, text="¿No tienes una cuenta?", font=("Arial", 16))
        register_label.pack()

        register_button = ctk.CTkButton(
            self, text="Registrarse", command=database.open_register, corner_radius=10)
        register_button.pack()

    def verificar_login(self):
        usuario = self.user_entry.get()
        contrasena = self.pass_entry.get()
        if database.validate_user_exists(usuario, contrasena):
            self.withdraw()
            root_tk = ctk.CTk()
            root_tk.geometry("600x600")
            root_tk.resizable(False, False)
            mensaje_bienvenida = ctk.CTkLabel(
                master=root_tk,
                text="¡Bienvenido " + usuario + "!",
                font=("Arial", 14)
            )
            root_tk.after(
                2000, lambda: [mensaje_bienvenida.configure(text="")])
            mensaje_bienvenida.pack(pady=10)
            boton_agregar = ctk.CTkButton(master=root_tk, text="cerrar", command=lambda: [
                                          self.destroy(), root_tk.destroy()], width=10, height=10, corner_radius=10)
            boton_agregar.pack(side="bottom", padx=10, pady=10)
            pswd.create_frame(root_tk)

            root_tk.mainloop()

        # frame donde van los entrys y los botones
        frame_login = ctk.CTkFrame(master=self.ventana)
        frame_login.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

        # frame del titulo
        frame_title = ctk.CTkFrame(
            master=frame_login)
        frame_title.pack(side=tk.TOP, fill=tk.X)
        # label del titulo
        label_title = ctk.CTkLabel(
            master=frame_title, text="Inicio de Sesion", font=("Times", 25))
        label_title.pack(expand=tk.YES, fill=tk.BOTH)
        user_label = ctk.CTkLabel(
            master=frame_login, text="Usuario", font=("Times", 15))
        user_label.pack(fill=tk.X, padx=20, pady=10)
        entry_user = ctk.CTkEntry(
            master=frame_login, placeholder_text="Usuario")
        entry_user.pack(fill=tk.X, padx=20, pady=10)

        passwd_label = ctk.CTkLabel(
            master=frame_login, text="contraseña", font=("Times", 15))
        passwd_label.pack(fill=tk.X, padx=20, pady=10)
        entry_password = ctk.CTkEntry(
            master=frame_login, placeholder_text="Contraseña", show="*")
        entry_password.pack(fill=tk.X, padx=20, pady=10)

        login_button = ctk.CTkButton(
            master=frame_login, text="Iniciar sesion", width=10, height=10, corner_radius=10)
        login_button.pack(padx=20, pady=20)
