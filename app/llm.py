import os
from app.config import settings


class LLM:
    def __init__(self):
        self._c = None
        self.mode = "mock"
        if settings.llm_ready:
            os.environ["GROQ_API_KEY"] = settings.groq_api_key
            from langchain_groq import ChatGroq
            self._c = ChatGroq(model=settings.groq_model, temperature=0.2)
            self.mode = "groq"

    def complete(self, p):
        return self._c.invoke(p).content if self._c else "MOCK: grounded answer using history and context."


llm = LLM()
