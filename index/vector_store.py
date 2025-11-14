import numpy as np
from dataclasses import dataclass
from sentence_transformers import SentenceTransformer
import faiss

@dataclass
class VSItem:
    pdf_name: str
    page_number: int
    text: str

class VectorStore:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer("all-MiniLM-L12-v2")

        self.items: list[VSItem] = []
        self.index = None
        self._dim = self.model.get_sentence_embedding_dimension()

    def add(self, items: list[VSItem]):
        self.items.extend(items)

    def build(self):
        texts = [it.text for it in self.items]
        print(f"Encoding {len(texts)} chunks... please wait ~{len(texts)//10 + 1} seconds")
        embs = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        print("✅ Embeddings created")

        self.index = faiss.IndexFlatIP(self._dim)
        self.index.add(embs.astype(np.float32))
        self._embs = embs  # keep if you want to append later

    def search(self, query: str, k: int = 6):
        q = self.model.encode([query], convert_to_numpy=True, normalize_embeddings=True).astype(np.float32)
        scores, idxs = self.index.search(q, k)
        results = []
        for i, s in zip(idxs[0], scores[0]):
            it = self.items[int(i)]
            results.append((float(s), it))
        return results
