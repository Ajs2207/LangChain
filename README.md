# LangChain
Different Langchain Components use cases.
1. Chatbot:
    This folder consists of implementation of OPENAI API and Ollama (For local model instance). This also consists of LANGSMITH integration where chat logs and statistics can be seen.

2. api:
    This folder consists of implementation of OPENAI API and Ollama (For local model instance). This also consists of LanfServe integration where api interaction with a simple frontend ui is demonstrated.

3. rag:
    This folder consists of implementation of OPENAI embeddings and Langchain document loader. This also consists of storing the vectors in chroma db and querying the db to get the output.

4. chain:
    This folder consists of implementation of OPENAI embeddings and Langchain's Retriever and Chains implementation. This also consists of storing the vectors in FAISS db and querying the db to get the output using retrieval-chain.

5. agents:
    This folder consists of implementation of Langchain Agents, where we have multiple data sources. Also it consists of implementation of how to create different tools using Langchain Framework.

6. groq:
    This folder consists of implementation of GROQ inference along with the use of Ollama Embeddings. Also created a simple ui using streamlit which also encompasses a Document similarity search.

7. huggingface:
    This folder consists of implementation of hugging face models(both llms and embedding models). Also created a RetrievalQA object to connect prompt template and llm.