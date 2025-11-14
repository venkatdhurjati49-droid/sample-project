from typing import Iterable
from dataclasses import dataclass

@dataclass
class Chunk:
    pdf_name: str
    page_number: int
    text: str

def chunk_pages(pages, max_chars: int = 2000, overlap: int = 0):

    for pg in pages:
        t = pg.text
        if not t: 
            continue
        start = 0
        while start < len(t):
            end = min(len(t), start + max_chars)
            yield Chunk(pg.pdf_name, pg.page_number, t[start:end])
            start = end - overlap
            if start < 0: start = 0
