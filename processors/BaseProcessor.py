from abc import ABC, abstractmethod


class BaseProcessor(ABC):
    @abstractmethod
    def extract(self, file_path: str) -> str:
        """Extrae el texto desde un archivo."""
        pass
