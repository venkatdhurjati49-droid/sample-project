from index.vector_store import VectorStore, VSItem

def make_index(chunks):
    vs = VectorStore()
    items = [VSItem(c.pdf_name, c.page_number, c.text) for c in chunks]
    vs.add(items)
    vs.build()
    return vs
