from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

class EmbeddingStore:
    def __init__(self):
        self.embedding_model = OpenAIEmbeddings(model='text-embedding-3-large')

    def store_chunks(self,chunks):
        texts = [chunk['content'] for chunk in chunks]

        metadatas = [
            {'file': chunk['file']} for chunk in chunks
        ]

        vector_store = QdrantVectorStore.from_texts(
            texts=texts,
            metadatas=metadatas,
            embedding=self.embedding_model,
            url="http://localhost:6333",
            collection_name="codebase_embeddings",
        )

        return vector_store