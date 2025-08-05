# 🤖 Product Assistant Chatbot using RAG

## 🧠 About Product Assistant RAG

The Product Assistant RAG is an intelligent chatbot built using Retrieval-Augmented Generation (RAG). It answers questions about the RVPro bot based on its hardware and software documentation. The chatbot uses Markdown (`.md`) files as the knowledge source for product specifications. It combines OpenAI’s GPT model with a local vector store for context-aware responses. This assistant helps users, developers, and support teams get quick and accurate product insights.

<p align="center">
  <img src="assets/output.gif" alt="Indoor Gear" width="100%" />
</p>

---

## 🔍 What is RAG?

RAG (Retrieval-Augmented Generation) is a method that combines document retrieval with text generation. It allows a language model to pull relevant context from a knowledge base before answering. This makes responses more accurate, up-to-date, and domain-specific. It’s especially useful in chatbots that need to answer based on custom data or documents.  
RAG systems typically use embeddings, vector databases, and LLMs together.

---

## 📁 Project Structure

```
PA_chatbot/
├── data/                  # Contains source Markdown files
│   ├── hardware.md        # Hardware specifications
│   └── software.md        # Software/firmware details
|   |__ code_helper.md     # Code Helper Doc
│
├── db/                    # Auto-generated vector DB by Chroma
│
├── ingest_data.py         # Script to load, split, and embed data into DB
├── app_main.py            # Streamlit chatbot app using LangChain RAG
├── .env                   # Contains OpenAI API key
├── requirements.txt       # List of required Python libraries
└── README.md              # Project documentation
```
---

## ⚙️ Working Procedure

### ✅ Step 1: Clone the Repository

```bash
clone this repository.
```

### ✅ Step 2: Install Required Libraries

Install all dependencies using:

```bash
pip install -r requirements.txt
```

### requirements.txt

```txt
langchain
openai
chromadb
tiktoken
python-dotenv
unstructured
markdown
streamlit
```

---

### ✅ Step 3: Prepare the Dataset

Place your product spec files in the `data/` folder:
- `hardware.md` for hardware details
- `software.md` for software/firmware specs
- `code_helper.md` for code helper

### ✅ Step 4: Add Your OpenAI API Key

Create a `.env` file in the project root with your key:

```env
OPENAI_API_KEY=your-openai-key-here
```

### ✅ Step 5: Run `ingest_data.py` to Build Vector DB

```bash
python ingest_data.py
```

### ✅ Step 6: Run the Chatbot

```bash
streamlit run app_main.py
```

### ✅ Step 7: Ask Questions

In your browser, try questions like:
- “What microcontroller does RVPro use?”
- “Does the bot support OTA updates?”
- “What motor driver is included?”

---

🔗 Built with **LangChain**, **OpenAI**, **ChromaDB**, and **Streamlit**  
🧠 Powered by **Retrieval-Augmented Generation**