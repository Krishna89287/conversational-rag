"""Per-session conversation memory and the document store with BM25 retrieval.
Memory is what makes follow-up questions like 'and the paid one?' work."""
from rank_bm25 import BM25Okapi

DOCS = [
    {"id": "D1", "text": "The free plan includes 3 projects and 1 GB storage."},
    {"id": "D2", "text": "The pro plan includes unlimited projects, 100 GB storage and priority support."},
    {"id": "D3", "text": "Annual billing gives a 20 percent discount over monthly billing."},
    {"id": "D4", "text": "You can cancel any time from Settings, and access continues until the period ends."},
]
_tok = [d["text"].lower().split() for d in DOCS]
_bm25 = BM25Okapi(_tok)
SESSIONS = {}


def retrieve(q, k=2):
    s = _bm25.get_scores(q.lower().split())
    order = sorted(range(len(DOCS)), key=lambda i: s[i], reverse=True)
    return [DOCS[i] for i in order[:k]]


def history(session_id):
    return SESSIONS.setdefault(session_id, [])


def remember(session_id, role, text):
    history(session_id).append({"role": role, "text": text})
