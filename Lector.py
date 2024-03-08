import PyPDF2

def leerPDF(nombres_archivos):
    textos_pdf = []
    for nombre_archivo in nombres_archivos:
        with open(nombre_archivo, 'rb') as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)
            numero_paginas = len(lector_pdf.pages)

            texto_completo = ""
            for pagina_numero in range(numero_paginas):
                pagina = lector_pdf.pages[pagina_numero]
                texto_completo += pagina.extract_text()

        textos_pdf.append(texto_completo)

    return textos_pdf
