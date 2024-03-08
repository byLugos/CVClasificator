# Importaciones necesarias
import tkinter as tk  # Módulo para la interfaz gráfica de usuario
from tkinter import messagebox, ttk  # Módulos para mostrar mensajes de aviso y crear widgets de ttk
from ttkthemes import ThemedStyle  # Módulo para aplicar temas a la interfaz gráfica
import Clasificador  # Módulo que contiene la lógica de clasificación de archivos


# Clase para la interfaz de bienvenida
class GUIBienvenida:
    # Constructor
    def __init__(self, raiz):
        # Configuración de la ventana principal
        self.raiz = raiz
        self.raiz.title("Bienvenido")
        self.raiz.geometry("600x500")
        self.raiz.configure(bg="light blue")  # Cambia "light blue" al color que desees
        self.clasificador = Clasificador.Clasificacion("Persistencia")

        # Etiqueta de bienvenida
        self.label = ttk.Label(self.raiz, text="Bienvenido al Clasificador de CV", font=("Helvetica", 22),
                               background="light gray")
        self.label.pack(pady=20)

        # Etiqueta de autores
        self.label_autores = ttk.Label(self.raiz,
                                       text="Creado por: Ian Rodríguez, Sebastián Garzón , Nicolas Laverde",
                                       font=("Helvetica", 12), background="light blue")
        self.label_autores.pack(pady=5)

        # Imagen del logo
        self.logo = tk.PhotoImage(file="Include/logo.png")
        self.logo = self.logo.subsample(2, 2)  # Redimensiona la imagen
        self.logo_label = ttk.Label(self.raiz, image=self.logo)
        self.logo_label.pack(pady=10)

        # Botón para seleccionar carpeta
        self.seleccionarCarpeta = ttk.Button(self.raiz, text="Seleccionar carpeta", command=self.seleccionarCarpeta)
        self.seleccionarCarpeta.pack(pady=10)

        # Botón para iniciar el programa
        self.estilo = ThemedStyle(self.raiz)
        self.estilo.set_theme("plastik")
        self.iniciar = ttk.Button(self.raiz, text="Comenzar", command=self.abrirVentanaMain)
        self.iniciar.pack()

        # Centra la ventana en la pantalla
        self.centrarVentana()

    # Método para abrir la ventana principal
    def abrirVentanaMain(self):
        self.raiz.withdraw()
        root = tk.Tk()
        app = GUI(root, self.clasificador.ruta_carpeta, self)

    # Método para seleccionar carpeta
    def seleccionarCarpeta(self):
        messagebox.showinfo("Aviso", "Se recomienda usar la carpeta 'PERSISTENCIA' por defecto")

    # Método para centrar la ventana en la pantalla
    def centrarVentana(self):
        self.raiz.eval('tk::PlaceWindow . center')


# Clase para la ventana principal
class GUI:
    # Constructor
    def __init__(self, raiz, carpeta, ventana):
        self.raizGUI = raiz
        self.raizGUI.title("Clasificador de CV")
        self.raizGUI.configure(bg="light blue")
        self.raizGUI.geometry("400x300")
        self.clasificador = Clasificador.Clasificacion(carpeta)
        self.vBienvenida = ventana
        self.estiloGUI = ThemedStyle(self.raizGUI)
        self.estiloGUI.set_theme("plastik")

        self.crearVentanas()

    # Método para crear los widgets de la ventana principal
    def crearVentanas(self):
        self.ventanaMain = ttk.Frame(self.raizGUI, padding="20")
        self.ventanaMain.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.ventanaMain.columnconfigure(0, weight=1)
        self.ventanaMain.rowconfigure(0, weight=1)

        ttk.Label(self.ventanaMain, text="Selecciona una opción para clasificar:", font=("Helvetica", 14),
                  background="light blue").grid(column=0, row=0, pady=10, sticky=tk.W)

        ttk.Button(self.ventanaMain, text="Clasificar por nivel de inglés (B1)",
                   command=lambda: self.clasiIngles("B1")).grid(column=0, row=1, pady=5, padx=10, sticky=tk.W)
        ttk.Button(self.ventanaMain, text="Clasificar por nivel de inglés (B2)",
                   command=lambda: self.clasiIngles("B2")).grid(column=0, row=2, pady=5, padx=10, sticky=tk.W)
        ttk.Button(self.ventanaMain, text="Clasificar por título profesional", command=self.clasiProfesion).grid(
            column=0, row=3, pady=5, padx=10, sticky=tk.W)

        ttk.Separator(self.ventanaMain, orient="horizontal").grid(column=0, row=4, pady=10, sticky="ew")

        ttk.Button(self.ventanaMain, text="Volver", command=self.irAtras).grid(column=0, row=5, pady=10, padx=10,
                                                                               sticky=tk.W)

        self.centrarVentana()

    # Método para volver a la ventana de bienvenida
    def irAtras(self):
        self.raizGUI.destroy()
        self.vBienvenida.raiz.deiconify()

    # Método para centrar la ventana en la pantalla
    def centrarVentana(self):
        self.raizGUI.eval('tk::PlaceWindow . center')

    # Método para mostrar un aviso
    def mostrarAviso(self, criterio):
        messagebox.showinfo("Aviso", f"Cierto/s PDF's no cumplieron con el criterio de búsqueda para {criterio}")

    # Método para clasificar por nivel de inglés
    def clasiIngles(self, level):
        try:
            self.clasificador.clasificarIngles(level)
            messagebox.showinfo("Clasificación completada",
                                f"Los archivos han sido clasificados en la carpeta 'NIVEL {level} INGLES'.")
            if not Clasificador.avisar():
                self.mostrarAviso("INGLÉS")
        except ValueError as e:
            messagebox.showerror("Error fatal", str(e))

    # Método para clasificar por título profesional
    def clasiProfesion(self):
        try:
            self.clasificador.clasificarCarrera()
            messagebox.showinfo("Clasificación completada",
                                f"Los archivos han sido clasificados en la carpeta PROFESIONALES en subcarpetas según su área de desempeño.")
            if not Clasificador.avisar():
                self.mostrarAviso("TÍTULO PROFESIONAL")
        except ValueError as e:
            messagebox.showerror("Error fatal", str(e))

# Función principal para ejecutar la aplicación
def main():
    root = tk.Tk()
    app = GUIBienvenida(root)
    root.mainloop()


if __name__ == "__main__":
    main()
