import tkinter as tk
from tkinter import messagebox
import Clasificador as clasif
class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Clasificador de CV")
        self.clasificadorIngles = clasif.Ingles("Persistencia")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Carpeta predeterminada: Persistencia")
        self.label.pack()

        self.b1_button = tk.Button(self.root, text="Clasificar por nivel de inglés (B1)", command=lambda: self.clasificar_ingles("B1"))
        self.b1_button.pack()

        self.b2_button = tk.Button(self.root, text="Clasificar por nivel de inglés (B2)", command=lambda: self.clasificar_ingles("B2"))
        self.b2_button.pack()

        self.other_button = tk.Button(self.root, text="Clasificar por otras categorías", command=self.etc)
        self.other_button.pack()

    def etc(self):
        # Aquí puedes agregar tu lógica para clasificar por otras categorías
        pass

    def clasificar_ingles(self, level):
        try:
            self.clasificadorIngles.clasificar(level)
            messagebox.showinfo("Clasificación completada", f"Los archivos han sido clasificados en la carpeta 'NIVEL {level} INGLES'.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()