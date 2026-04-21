from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

class Retriever:
    def __init__(self):
        self.embedding_model = OpenAIEmbeddings(model='text-embedding-3-large')

        self.vector_store = QdrantVectorStore.from_existing_collection(
            embedding=self.embedding_model,
            url="http://localhost:6333",
            collection_name="codebase_embeddings"
        )

    def search(self,query,k=5):
        retriever = self.vector_store.as_retriever(search_kwargs={'k':k})
        return retriever.invoke(query)