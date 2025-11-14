import os
from pathlib import Path
from dotenv import load_dotenv
from rich import print

from ingest.pdf_loader import load_many
from ingest.chunker import chunk_pages
from index.build_index import make_index
from agent.qa_agent import answer_query
from agent.schema import QAJson

def build_pipeline(pdf_dir: str):
    print("Loading PDFs...")
    pages = load_many(Path(pdf_dir))
    print(f"{len(pages)} pages loaded")

    print("Chunking...")
    chunks = list(chunk_pages(pages))
    print(f"{len(chunks)} chunks created")

    print("Building index...")
    vs = make_index(chunks)
    print("Index built!")
    return vs

def main():
    from pathlib import Path
    load_dotenv(dotenv_path=Path(__file__).parent / ".env")

    vs = build_pipeline("demo_pdfs")

    print("[bold green]PDFs indexed. Ask a question (or 'exit'):[/bold green]")
    while True:
        q = input("> ").strip()
        if not q or q.lower() in {"exit","quit"}:
            break
        try:
            result: QAJson = answer_query(q, vs, QAJson.model_json_schema())
            print(result.model_dump_json(indent=2))
        except Exception as e:
            print(f"[red]Error:[/red] {e}")

if __name__ == "__main__":
    main()
