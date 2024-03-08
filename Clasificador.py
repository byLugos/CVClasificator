import re
import os
import Lector as l  # Importa el módulo Lector como l
import ftplib  # Importa el módulo ftplib para trabajar con FTP

def avisar():
    return False  # Función que simplemente devuelve False

class Clasificacion:
    # Constructor de la clase
    def __init__(self, ruta_carpeta):
        self.ruta_carpeta = ruta_carpeta  # Guarda la ruta de la carpeta
        self.servidorFTP = "192.168.18.87"  # Dirección del servidor FTP
        self.user = "user"  # Nombre de usuario para el FTP
        self.password = "admin"  # Contraseña para el FTP

    # Método que retorna todos los PDF'S en una lista
    def enviarNombres(self, dPrincipal):
        # Obtiene la lista de nombres de archivos PDF en la carpeta especificada
        nombresArchivos = [os.path.join(dPrincipal, archivo) for archivo in os.listdir(dPrincipal) if
                           archivo.endswith(".pdf")]
        # Lee los PDFs y devuelve una lista de documentos
        documentos = l.leerPDF(nombresArchivos)
        return documentos

    # Método que retorna el nombre de cada uno de los PDF en la carpeta principal
    def nombreArchivos(self, dPrincipal):
        # Obtiene la lista de nombres de archivos PDF en la carpeta especificada
        nombresArchivos = [os.path.join(dPrincipal, archivo) for archivo in os.listdir(dPrincipal) if
                           archivo.endswith(".pdf")]
        if nombresArchivos:  # Verifica si la lista de nombres de archivos no está vacía
            return nombresArchivos  # Devuelve la lista de nombres de archivos
        else:
            raise ValueError("NO SE HAN ENCONTRADO PDF'S A EVALUAR EN LA CARPETA")  # Lanza un error si no se encuentran archivos PDF

    # Método que clasifica y agrega PDF según el nivel de inglés
    def clasificarIngles(self, level):
        # Directorio principal
        directorioPrincipal = self.ruta_carpeta
        # Nombre de los archivos
        nombreArchivos = self.nombreArchivos(directorioPrincipal)

        # Carpetas donde se guardarán los PDF
        directorioB1 = "CV/NIVEL B1 INGLES"
        directorioB2 = "CV/NIVEL B2 INGLES"

        # Regex para buscar palabra INGLÉS
        buscarIngles = re.compile(r'INGLES?:?\s*', re.IGNORECASE)
        buscarInglesAlt = re.compile(r'INGLÉS?:?\s*', re.IGNORECASE)

        # Lista que guardará los PDF's clasificados
        b1Clasificados = []
        b2Clasificados = []

        # Clasificación de PDF's
        for i, documento in enumerate(self.enviarNombres(directorioPrincipal)):
            if buscarIngles.search(documento) or buscarInglesAlt.search(documento):
                if level == "B1" and "B1" in documento:
                    print("ENCONTRÓ UN NIVEL B1 EN EL PDF ", i + 1)
                    b1Clasificados.append(nombreArchivos[i])
                    self.enviarPDF(b1Clasificados, self.servidorFTP, self.user, self.password, directorioB1)
                elif level == "B2" and "B2" in documento:
                    print("ENCONTRÓ UN NIVEL B2 EN EL PDF ", i + 1)
                    b2Clasificados.append(nombreArchivos[i])
                    self.enviarPDF(b2Clasificados, self.servidorFTP, self.user, self.password, directorioB2)
            else:
                print("NO HAY NIVEL DE INGLÉS EN EL PDF ", i + 1)
                avisar()

    # Método que clasifica por carrera profesional
    def clasificarCarrera(self):
        # Directorio principal
        directorioPrincipal = self.ruta_carpeta
        # Nombre de los archivos
        nombreArchivos = self.nombreArchivos(directorioPrincipal)

        # Patrones para buscar en el contenido de los PDF
        patrones = {
            r'(Ingenier[ií]a|Desarrollador[ra]?|Electr[oó]nica|El[eé]ctrica|Programador)': "CV/PROFESIONALES/Ingenieria y Tecnologia",
            r'(Administraci[oó]n|Administrador[a]?|Contador[a]?|Marketing|Econom[ií]a|Economia|Economista)': "CV/PROFESIONALES/Negocios y Administracion",
            r'(Recursos\shumanos|Contrataci[oó]n)': "CV/PROFESIONALES/Recursos y Humanidades",
            r'(Matem[aá]tic[oa]s?|F[ií]sic[oa])': "CV/PROFESIONALES/Ciencias"
        }

        # Clasificación de PDF's por carrera profesional
        for i, documento in enumerate(self.enviarNombres(directorioPrincipal)):
            for patron, directorio in patrones.items():
                if re.search(patron, documento):
                    self.enviarPDF([nombreArchivos[i]], self.servidorFTP, self.user, self.password, directorio)
                    break
            else:
                print("NO HAY CRITERIO DE BÚSQUEDA ENCONTRADO EN EL PDF ", i + 1)
                avisar()

    # Método que agrega los archivos al servidor FTP
    def enviarPDF(self, lista, servidor_ftp, usuario, contrasenha, destino_ftp):
        try:
            with ftplib.FTP(servidor_ftp, usuario, contrasenha) as ftp:
                # Intenta cambiar al directorio de destino
                try:
                    ftp.cwd(destino_ftp)
                except ftplib.error_perm:
                    # Si el directorio no existe, se intenta crearlo
                    try:
                        print("La carpeta no existe, se creará")
                        ftp.mkd(destino_ftp)
                        print(f"Se creó el directorio {destino_ftp} en el servidor FTP.")
                        ftp.cwd(destino_ftp)  # Cambia al nuevo directorio creado
                    except ftplib.error_perm as e:
                        print(f"No se pudo crear el directorio {destino_ftp}: {e}")
                        raise ValueError("La carpeta no existe, no se pudo crear")

                # Ahora que estamos en el directorio de destino o se ha creado uno nuevo, procedemos con la transferencia de archivos
                for nombreArchivo in lista:
                    try:
                        with open(nombreArchivo, 'rb') as archivo:
                            ftp.storbinary(f'STOR {nombreArchivo}', archivo)
                        print(f"El archivo {nombreArchivo} ha sido enviado exitosamente a {servidor_ftp}/{destino_ftp}")
                    except ftplib.error_perm as e:
                        print(f"No se pudo enviar el archivo {nombreArchivo}: {e}")
                        raise ValueError(f"Ocurrió un error al enviar el archivo {nombreArchivo}: {e}")
                    except Exception as e:
                        print(f"Ocurrió un error al enviar el archivo {nombreArchivo}: {e}")
                        raise ValueError(f"Ocurrió un error al enviar el archivo {nombreArchivo}: {e}")
        except ftplib.all_errors as e:
            print(f"Error de conexión FTP: {e}")