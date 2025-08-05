import streamlit as st
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

PERSIST_DIR = "chroma_db"

@st.cache_resource
def load_chain():
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=PERSIST_DIR, embedding_function=embedding)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
    return chain

def main():
    st.set_page_config(page_title="RVPro Assistant", page_icon="🤖")
    st.title("🤖 RVPro Product Assistant")
    st.caption("Ask me anything about the 4-wheel RVPro bot (hardware/software specs)")

    query = st.text_input("Your question:", placeholder="e.g., What is the motor type?")
    if query:
        with st.spinner("Thinking..."):
            chain = load_chain()
            answer = chain.run(query)
            st.success(answer)

if __name__ == "__main__":
    main()
