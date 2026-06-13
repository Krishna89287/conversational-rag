from fastapi import FastAPI
from pydantic import BaseModel
from app.store import retrieve, history, remember
from app.llm import llm

app = FastAPI(title="Conversational RAG", version="1.0.0",
              description="Multi-turn chat-with-your-docs: keeps session memory, rewrites follow-ups using history, retrieves and answers with citations.")


class Turn(BaseModel):
    session_id: str
    message: str


@app.get("/health")
def health():
    return {"status": "ok", "llm_mode": llm.mode}


@app.post("/chat")
def chat(t: Turn):
    hist = history(t.session_id)
    hist_text = " | ".join(f"{h['role']}: {h['text']}" for h in hist[-4:])
    docs = retrieve(t.message + " " + hist_text)
    context = "\n".join(f"[{d['id']}] {d['text']}" for d in docs)
    prompt = ("Continue the conversation. Use the history to resolve follow-up references, "
              "answer only from the context, and cite source ids.\n"
              f"History: {hist_text}\nContext:\n{context}\nUser: {t.message}")
    answer = llm.complete(prompt)
    remember(t.session_id, "user", t.message)
    remember(t.session_id, "assistant", answer)
    return {"answer": answer, "citations": [d["id"] for d in docs], "turns": len(history(t.session_id)) // 2}
