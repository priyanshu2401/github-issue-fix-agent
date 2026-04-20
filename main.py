from agents.code_reader import CodeReader

reader = CodeReader(".")
codebase = reader.load_codebase()

chunks = reader.chunk_code(codebase)

print(f"Total chunks: {len(chunks)}")

for chunk in chunks[:3]:
    print("\n---")
    print(chunk["file"])
    print(chunk["content"][:200])