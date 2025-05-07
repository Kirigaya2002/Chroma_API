import os

# Guarda un archivo temporal y devuelve su ruta  
def save_temp_file(filename: str, content: bytes) -> str:
    file_path = f"./temp_{filename}"
    with open(file_path, "wb") as f:
        f.write(content)
    return file_path

# Elimina un archivo temporal si existe
def delete_temp_file(path: str):
    if os.path.exists(path):
        os.remove(path)