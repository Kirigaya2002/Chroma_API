import fitz  # PyMuPDF

def extraer_texto_pdf(ruta):
    texto = ""
    with fitz.open(ruta) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto