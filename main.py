from agents.code_reader import CodeReader
from tools.embedding_store import EmbeddingStore
from tools.retriever import Retriever

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

print("✅ Embeddings stored successfully!")

retriever = Retriever()

results = retriever.search("read files from directory")

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print("File:", doc.metadata.get("file"))
    print(doc.page_content[:200])