from pydantic import BaseModel, Field
from typing import List

class Reference(BaseModel):
    pdf: str
    page: int
    snippet: str

class AnswerItem(BaseModel):
    answer: str
    confidence: float = Field(ge=0, le=1)
    references: List[Reference]

class QAJson(BaseModel):
    query: str
    answers: List[AnswerItem]
