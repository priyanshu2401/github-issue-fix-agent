from openai import OpenAI
from tools.retriever import Retriever

client = OpenAI()

class RAGEngine:
    def __init__(self):
        self.retriever = Retriever()

    def answer(self,query):
        docs = self.retriever.search(query)

        context = context = "\n\n\n".join([
            f"[File: {doc.metadata.get('file')}]\n{doc.page_content}"
            for doc in docs
        ])

        SYSTEM_PROMPT = f"""
        You are a senior software engineer.

        Answer the user's question using ONLY the provided code context.

        If the answer is not in the context, say:
        "Not found in codebase."

        Be precise and technical.

        Context:
        {context}
        """

        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role':'system','content':SYSTEM_PROMPT},
                {'role':'user','content':query}
            ]
        )

        return response.choices[0].message.content