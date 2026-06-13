# Conversational RAG (Chat with your docs)

A multi-turn Retrieval Augmented Generation chat that remembers the conversation.
It keeps per-session history, uses it to resolve follow-up references like "and the
pro one?", retrieves the right documents, and answers with citations.

## Why it is useful for companies
Real users ask follow-up questions. A single-shot RAG bot loses the thread and
forces users to repeat context. This keeps session memory so the assistant feels
like a real conversation, while every answer still cites its sources.

## What it does
- Per-session conversation memory
- Follow-up resolution using recent history
- BM25 retrieval with citations
- Grounded, cited answers

## Quickstart
```bash
make install
make run     # http://localhost:8040
curl -s -X POST localhost:8040/chat -H "content-type: application/json" \
  -d '{"session_id":"s1","message":"What is in the free plan?"}'
curl -s -X POST localhost:8040/chat -H "content-type: application/json" \
  -d '{"session_id":"s1","message":"and the pro one?"}'
```
Runs in mock mode with no key. Add GROQ_API_KEY in .env for real answers.

## Stack
Python, FastAPI, session memory, BM25 retrieval, Groq LLM (optional), Docker, GitHub Actions CI, Pytest.

## License
MIT
