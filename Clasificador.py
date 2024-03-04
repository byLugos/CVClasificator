import re
import os
import shutil
import Lector as l

class Metodo:
    def __init__(self, ruta_carpeta):
        self.ruta_carpeta = ruta_carpeta
    def clasificarIngles(self, level):
        buscarIngles = re.compile(r'INGLES?:?\s*', re.IGNORECASE)
        buscarInglesAlt = re.compile(r'INGLÉS?:?\s*', re.IGNORECASE)

        #CARPETA A ENVIAR AL SERVIDOR
        carpetaB1 = 'NIVEL B1 INGLES'
        carpetaB2 = 'NIVEL B2 INGLES'

        if not os.path.isdir(self.ruta_carpeta):
            raise ValueError("La carpeta no existe.")

        for nombreArchivo in os.listdir(self.ruta_carpeta):
            if nombreArchivo.endswith('.pdf'):
                rutaCompleta = os.path.join(self.ruta_carpeta, nombreArchivo)
                texto = l.leerPDF(rutaCompleta)

                if buscarIngles.search(texto) or buscarInglesAlt.search(texto):
                    if level == "B1" and "B1" in texto:
                        print(f"Copiando el archivo {nombreArchivo} a la carpeta de B1...")
                        #shutil.copy(rutaCompleta, carpetaB1)
                        print("¡Archivo copiado con éxito!\n")
                    elif level == "B2" and "B2" in texto:
                        print(f"Copiando el archivo {nombreArchivo} a la carpeta de B2...")
                        #shutil.copy(rutaCompleta, carpetaB2)
                        print("¡Archivo copiado con éxito!\n")
                else:
                    print("NO HAY NIVEL DE INGLÉS REGISTRADO EN EL PDF", nombreArchivo)

    def clasificarExp(self):
        buscarExp = re.compile(r'experiencia|historial|trayectoria', re.IGNORECASE)
        totalAnho = 0
        totalSemana = 0

        if not os.path.isdir(self.ruta_carpeta):
            raise ValueError("La carpeta no existe.")

        for nombreArchivo in os.listdir(self.ruta_carpeta):
            if nombreArchivo.endswith('.pdf'):
                rutaCompleta = os.path.join(self.ruta_carpeta, nombreArchivo)
                texto = l.leerPDF(rutaCompleta)

                if buscarExp.search(texto):
                    # Buscar números que representen años y semanas de experiencia
                    anos = re.findall(r'(\d+)\s+años?', texto)
                    semanas = re.findall(r'(\d+)\s+semanas?', texto)

                    # Sumar los años y semanas encontrados
                    if anos:
                        totalAnho += sum(map(int, anos))
                    if semanas:
                        totalSemana += sum(map(int, semanas))

        print(f"Total de experiencia: {totalAnho} años y {totalSemana} semanas.")
