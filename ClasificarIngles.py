import re
import shutil
import os
import Lector as l
# Ruta de la carpeta que contiene los archivos PDF
carpetaOriginal = 'Persistencia'

# Ruta de la carpeta donde se van a guardar INGLES B1
carpetaB1 = 'NIVEL B1 INGLES'

# Ruta de la carpeta donde se van a guardar INGLES B2
carpetaB2 = 'NIVEL B2 INGLES'

# Expresión regular para buscar "INGLES: INGLES ingles InGlEs iNgLeS"
buscarIngles = re.compile(r'INGLES?:?\s*', re.IGNORECASE)

# Expresión regular para buscar lo de arriba pero con tílde
buscarInglesDos = re.compile(r'INGLÉS?:?\s*', re.IGNORECASE)

# Expresión regular para buscar "B1" o "B2"
buscarB1 = re.compile(r'B1', re.IGNORECASE)
buscarB2 = re.compile(r'B2', re.IGNORECASE)

# Iterar sobre todos los archivos en la carpeta de origen
for nombre_archivo in os.listdir(carpetaOriginal):
    if nombre_archivo.endswith('.pdf'):  #Buscar los PDF
        ruta_completa = os.path.join(carpetaOriginal, nombre_archivo)
        texto = l.leerPDF(ruta_completa)

        if buscarIngles.search(texto) or buscarInglesDos.search(texto):
            if buscarB1.search(texto):
                print(f"Copiando el archivo {nombre_archivo} a la carpeta de B1...")
                shutil.copy(ruta_completa, carpetaB1)
                print("¡Archivo copiado con éxito!\n")
            elif buscarB2.search(texto):
                print(f"Copiando el archivo {nombre_archivo} a la carpeta de B2...")
                shutil.copy(ruta_completa, carpetaB2)
                print("¡Archivo copiado con éxito!\n")