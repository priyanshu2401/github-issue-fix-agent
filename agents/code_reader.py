from pathlib import Path

class CodeReader:
    def __init__(self,repo_path):
        self.repo_path = Path(repo_path)

    def get_all_files(self):
        files = []
        for file in self.repo_path.rglob("*"):
            if file.is_file() and not self._ignore_file(file):
                files.append(file)
        return files
    
    def _ignore_file(self,file):
        ignore_patterns = [
            ".git",
            "__pycache__",
            ".venv",
            "node_modules",
            ".DS_Store"
        ]
        return any(part in str(file) for part in ignore_patterns)
    
    def read_file(self,file):
        try:
            return file.read_text(encoding="utf-8")
        except Exception:
            return ""

    def load_codebase(self):
        codebase = {}

        files = self.get_all_files()

        for file in files:
            content = self.read_file(file)
            if content:
                codebase[str(file)] = content

        return codebase
    
    def chunk_code(self,codebase,chunk_size=1000,overlap=400):
        chunks = []

        for file_name, content in codebase.items():
            start = 0

            while start < len(content):
                chunk = content[start:start + chunk_size]
                chunks.append({
                    "file": file_name,
                    "content": chunk
                })
                start += chunk_size - overlap

        return chunks