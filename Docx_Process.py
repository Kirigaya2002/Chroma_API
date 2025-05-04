import docx

def extraer_texto_docx(ruta):
    doc = docx.Document(ruta)
    return "\n".join([p.text for p in doc.paragraphs])