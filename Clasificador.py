import re
import os
import Lector as l

class Ingles:
    def __init__(self, ruta_carpeta):
        self.ruta_carpeta = ruta_carpeta

    def clasificar(self, level):
        buscar_ingles = re.compile(r'INGLES?:?\s*', re.IGNORECASE)
        buscar_ingles_dos = re.compile(r'INGLÉS?:?\s*', re.IGNORECASE)
        carpeta_b1 = 'NIVEL B1 INGLES'
        carpeta_b2 = 'NIVEL B2 INGLES'

        if not os.path.isdir(self.ruta_carpeta):
            raise ValueError("La carpeta no existe.")

        for nombre_archivo in os.listdir(self.ruta_carpeta):
            if nombre_archivo.endswith('.pdf'):
                ruta_completa = os.path.join(self.ruta_carpeta, nombre_archivo)
                texto = l.leerPDF(ruta_completa)

                if buscar_ingles.search(texto) or buscar_ingles_dos.search(texto):
                    if level == "B1" and "B1" in texto:
                        print(f"Copiando el archivo {nombre_archivo} a la carpeta de B1...")
                        # shutil.copy(ruta_completa, carpeta_b1)
                        print("¡Archivo copiado con éxito!\n")
                    elif level == "B2" and "B2" in texto:
                        print(f"Copiando el archivo {nombre_archivo} a la carpeta de B2...")
                        # shutil.copy(ruta_completa, carpeta_b2)
                        print("¡Archivo copiado con éxito!\n")
                else:
                    print("NO HAY NIVEL DE INGLÉS REGISTRADO EN EL PDF", nombre_archivo)
