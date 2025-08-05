import os
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

DATA_FOLDER = "docs"
PERSIST_DIR = "chroma_db"

def load_documents():
    documents = []
    for file in os.listdir(DATA_FOLDER):
        if file.endswith(".md"):
            path = os.path.join(DATA_FOLDER, file)
            loader = UnstructuredMarkdownLoader(path)
            documents.extend(loader.load())
    return documents

def ingest():
    print("[INFO] Loading markdown documents...")
    docs = load_documents()
    print(f"[INFO] Loaded {len(docs)} document(s).")

    print("[INFO] Splitting documents...")
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(docs)

    print("[INFO] Creating vector embeddings...")
    vectorstore = Chroma.from_documents(
        documents=texts,
        embedding=OpenAIEmbeddings(),
        persist_directory=PERSIST_DIR
    )

    vectorstore.persist()
    print("[SUCCESS] Vector store saved to:", PERSIST_DIR)

if __name__ == "__main__":
    ingest()
