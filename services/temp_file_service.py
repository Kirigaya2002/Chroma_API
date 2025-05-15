import os
from config.settings import TEMP_FILE_PREFIX

class TempFileService:
    """Servicio para manejar archivos temporales."""

    @staticmethod
    def save_temp_file(filename: str, content: bytes) -> str:
        """Guarda un archivo temporal y devuelve su ruta."""
        file_path = f"./{TEMP_FILE_PREFIX}{filename}"
        with open(file_path, "wb") as f:
            f.write(content)
        return file_path

    @staticmethod
    def delete_temp_file(path: str) -> None:
        """Elimina un archivo temporal si existe."""
        if os.path.exists(path):
            os.remove(path)

    @staticmethod
    def delete_temp_files(paths: list[str]) -> None:
        """Elimina múltiples archivos temporales."""
        for path in paths:
            TempFileService.delete_temp_file(path)