from agents.code_reader import CodeReader

reader = CodeReader(repo_path=".")
codebase = reader.load_codebase()

for path, content in list(codebase.items())[:5]:
    print(f"\n--- {path} ---\n")
    print(content[:200])