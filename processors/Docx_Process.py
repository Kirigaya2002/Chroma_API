import docx
from processors.BaseProcessor import BaseProcessor

class DocxProcessor(BaseProcessor):
    def extract(self, file_path: str) -> str:
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])