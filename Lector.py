import PyPDF2

def leerPDF(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        numero_paginas = len(lector_pdf.pages)

        texto_completo = ""
        for pagina_numero in range(numero_paginas):
            pagina = lector_pdf.pages[pagina_numero]
            texto_completo += pagina.extract_text()

    return texto_completo
