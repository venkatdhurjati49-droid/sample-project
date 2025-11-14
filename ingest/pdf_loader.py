from dataclasses import dataclass
from pathlib import Path
import fitz  # PyMuPDF

@dataclass
class Page:
    pdf_name: str
    page_number: int  # 1-based
    text: str

def load_pdf(path: Path) -> list[Page]:
    doc = fitz.open(path)
    pages = []
    for i in range(len(doc)):
        text = doc[i].get_text("text")
        pages.append(Page(pdf_name=path.name, page_number=i+1, text=text.strip()))
    return pages

def load_many(pdf_dir: Path) -> list[Page]:
    pages: list[Page] = []
    for p in sorted(pdf_dir.glob("*.pdf")):
        pages.extend(load_pdf(p))
    return pages
