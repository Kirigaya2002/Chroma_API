# Text Chunker
# parametro chunk_size: tamaño del chuck
# parametro overlap: sobrelaparción entre chucks para evitar perdida de contexto
def split_into_chunks(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks