"""importamos la libreria Customtkinter, y la libreria watchdog"""
import customtkinter as ctk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Monitor de archivos")
        self.geometry("750x270")
        self.resizable(True, False)
        self.entry1()
        self.frame1()
        self.label_1()
        self.buton_1()
        self.buton_2()
        self.mostrar_texto()

    def entry1(self):    # crear el entry de ruta
        """crear el entry de ruta, recibe como parametro la unidad a monitorear"""
        self.entry = ctk.CTkEntry(
            master=self, placeholder_text="Ingrese la ruta a monitorear")
        self.entry.pack(side="top", padx=10, pady=10)
        self.entry.configure(
            width=400, height=15)

    def frame1(self):
        """es el frame que mantiene al label"""
        # crear el frame
        self.frame = ctk.CTkFrame(
            master=self,  corner_radius=10)
        self.frame.pack(fill="x", expand=True)

    def label_1(self):
        """crear el label donde se muestran los datos"""
        # crear el label donde se muestran los datos
        self.label1 = ctk.CTkLabel(
            master=self.frame, text="", font=("Arial", 15), corner_radius=10, width=700, height=180)
        self.label1.pack(fill="x", expand=True)
        self.value = None

    def buton_1(self):
        # Crear un botón personalizado y agregarlo a la cuadrícula
        self.button = ctk.CTkButton(
            master=self, text="Ver ruta", command=self.mostrar_texto)
        self.button.pack(anchor="s", side="left", padx=10, pady=5)
        self.button.configure(
            width=20, height=30)

    def buton_2(self):
        self.button = ctk.CTkButton(
            master=self, text="Analizar", command=self.iniciar_dog)
        self.button.pack(anchor="s", side="left", padx=10, pady=5)
        self.button.configure(
            width=20, height=30, fg_color="red")

    def mostrar_texto(self):
        self.value = self.entry.get()
        self.label1.configure(text="Ruta a analizar : " + self.value)

    def iniciar_dog(self):
        dog_instance = Dog(self.value, self.label1)
        dog_instance.dogo()


class Dog(FileSystemEventHandler):
    def __init__(self, texto, label1) -> None:
        super().__init__()
        self.value = texto
        texto = self.value
        self.label1 = label1

    def on_created(self, event):
        self.label1.configure(text="Creado : \n " + event.src_path)

    def on_modified(self, event):
        self.label1.configure(text="Modificado : \n " + event.src_path)

    def on_moved(self, event):
        self.label1.configure(text="Movido a :\n" + event.src_path +
                              event.dest_path)

    def on_deleted(self, event):
        self.label1.configure(text="Borrado : \n" + event.src_path)

    def dogo(self):
        observer = Observer()
        observer.schedule(self, self.value, recursive=True)
        observer.start()


ventana = Root()
ventana.mainloop()
