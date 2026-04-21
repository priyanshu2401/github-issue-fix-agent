from agents.code_reader import CodeReader
from tools.embedding_store import EmbeddingStore
from tools.retriever import Retriever
from tools.rag_engine import RAGEngine

reader = CodeReader(".")
codebase = reader.load_codebase()

chunks = reader.chunk_code(codebase)

print(f"Total chunks: {len(chunks)}")

# for chunk in chunks[:10]:
#     print("\n---")
#     print(chunk["file"])
#     print(chunk["content"][:200])

store = EmbeddingStore()
vector_db = store.store_chunks(chunks)

rag = RAGEngine()

while True:
    query = input("\nAsk about your codebase: ")

    if query.lower() in ["exit", "quit", "bye"]:
        break

    answer = rag.answer(query)

    print("\n🤖 Answer:\n", answer)