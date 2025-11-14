from typing import List
from agent.llm import ask_json
from agent.schema import QAJson
from textwrap import dedent

def build_prompt(query: str, retrieved):
    # retrieved: list[(score, VSItem)]
    context_blocks = []
    for score, it in retrieved:
        context_blocks.append(
            f"[{it.pdf_name} p.{it.page_number}] {it.text.strip()}"
        )
    context = "\n\n".join(context_blocks[:8])

    system_rules = dedent("""
    You are a precise PDF QA agent. 
    - Use ONLY the provided context to answer. If unknown, say "I don't know".
    - Always output strict JSON matching the provided schema.
    - Provide 1 concise answer with 2–4 references (pdf, page, snippet).
    - Confidence is 0.0–1.0 reflecting how well context supports the answer.
    """)

    user_task = f"Question: {query}\n\nContext:\n{context}\n\nAnswer in JSON."
    return f"{system_rules}\n\n{user_task}"

def answer_query(query: str, vs, schema_dict: dict) -> QAJson:
    retrieved = vs.search(query, k=8)
    prompt = build_prompt(query, retrieved)
    raw = ask_json(prompt, schema_dict)
    return QAJson.model_validate_json(raw)
