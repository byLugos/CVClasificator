import tkinter as tk
from tkinter import messagebox, ttk
import Clasificador as clasif
class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Clasificador de CV")
        self.clasificador = clasif.Metodo("Persistencia")
        self.crearVentanas()

    def crearVentanas(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.main_frame.columnconfigure(0, weight=1)

        self.label = ttk.Label(self.main_frame, text="Carpeta predeterminada: Persistencia")
        self.label.grid(column=0, row=0, columnspan=2, pady=(0, 10))

        self.b1_button = ttk.Button(self.main_frame, text="Clasificar por nivel de inglés (B1)", command=lambda: self.ClasifIngles("B1"))
        self.b1_button.grid(column=0, row=1, pady=5, sticky=tk.W+tk.E)

        self.b2_button = ttk.Button(self.main_frame, text="Clasificar por nivel de inglés (B2)", command=lambda: self.ClasifIngles("B2"))
        self.b2_button.grid(column=1, row=1, pady=5, sticky=tk.W+tk.E)

        self.b3_button = ttk.Button(self.main_frame, text="Clasificar por tiempo de experiencia", command=lambda: self.ClasifExp())
        self.b3_button.grid(column=2, row=1, pady=5, sticky=tk.W+tk.E)

        for child in self.main_frame.winfo_children():
            child.grid_configure(padx=10)

        self.centrarVentana()

    def centrarVentana(self):
        # Obtener el ancho y alto de la pantalla
        ancho = self.root.winfo_screenwidth()
        alto = self.root.winfo_screenheight()

        # Obtener el ancho y alto de la ventana
        anchoPantalla = self.root.winfo_reqwidth()
        altoPantalla = self.root.winfo_reqheight()

        # Calcular las coordenadas x y y para centrar la ventana
        x = int((ancho / 2) - (anchoPantalla / 2))
        y = int((alto / 2) - (altoPantalla / 2))

        # Establecer la geometría de la ventana
        self.root.geometry(f"+{x}+{y}")


    def ClasifIngles(self, level):
        try:
            #Llamar a la clase clasificador, específicamente la de inglés
            self.clasificador.clasificarIngles(level)
            #Si sale bien, sale clasificación completa
            messagebox.showinfo("Clasificación completada", f"Los archivos han sido clasificados en la carpeta 'NIVEL {level} INGLES'.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def ClasifExp(self):
        try:
            #Llamar a la clase clasificador, específicamente la de inglés
            self.clasificador.clasificarExp()
            #Si sale bien, sale clasificación completa
            messagebox.showinfo("Clasificación completada", f"Los archivos han sido clasificados en la carpeta 'AÑOS'")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()