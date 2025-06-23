# 🤖 GitLab GenAI Chatbot

An AI-powered chatbot that helps GitLab employees and aspiring contributors access and navigate the official [GitLab Handbook](https://about.gitlab.com/handbook/) and [GitLab Direction](https://about.gitlab.com/direction/) pages. Built using **LangChain**, **FAISS**, and **Gemini 1.5 Flash**, and deployed with **Streamlit**.

---

## 📌 Project Goal

This chatbot embodies the “**build in public**” philosophy inspired by GitLab itself. It enables:

- Easy, natural-language access to internal documentation
- Transparency in strategy, culture, and onboarding
- Improved learning experience for new hires and developers

---

## 🚀 Features

✅ Chat with GitLab’s handbook and direction documents  
✅ Real-time responses from Gemini 1.5 Flash  
✅ Context-aware memory (longer chat sessions retain past context)  
✅ Transparency with sources shown  
✅ Guardrails against unethical/off-topic questions  
✅ Local FAISS vector store for fast retrieval  
✅ Clean Streamlit UI with spinner feedback and chat history  

---

## 🛠️ Tech Stack

- `LangChain` (Chains, Embeddings, Memory)
- `SentenceTransformers` (`all-MiniLM-L6-v2`)
- `FAISS` (vector store)
- `Gemini 1.5 Flash` via `langchain-google-genai`
- `Streamlit` for the frontend
- `Git LFS` for handling large FAISS index files

---

## 📁 Folder Structure

```

├── chatApp.py                # Streamlit frontend app
├── build\_vector\_store.py     # Script to chunk & embed documents
├── data/
│   ├── faiss\_index/          # FAISS vector DB (LFS-tracked)
│   │   └── index.faiss
│   ├── handbook\_cleaned\_FULL.txt
│   └── direction\_final.txt
├── requirements.txt
├── .gitattributes            # Tracks FAISS via Git LFS
└── .streamlit/
└── secrets.toml          # API key (local only)

````

---

## ⚙️ Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone 
cd git-lab-chatbot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Enable Git LFS (for FAISS index)

```bash
git lfs install
git lfs pull
```

### 4. Add your Google API Key

Create a file:

```
.streamlit/secrets.toml
```

Paste your key:

```toml
GOOGLE_API_KEY = "your_api_key_here"
```

### 5. Run the chatbot

```bash
streamlit run chatApp.py
```

---

## 📄 Optional: Rebuild the Vector Store

To regenerate the FAISS index from raw text files:

```bash
python build_vector_store.py
```

Make sure your `data/handbook_cleaned_FULL.txt` and `data/direction_final.txt` exist.

---

## 🌐 Public Deployment

This chatbot is **Streamlit Cloud-ready**. Just:

1. Push to a public GitHub repo
2. Add the `GOOGLE_API_KEY` via [Streamlit Secrets](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app)
3. Click “Deploy” at [https://streamlit.io/cloud](https://streamlit.io/cloud)

---

## 🧪 Sample Questions to Test

```text
1. What are GitLab's communication principles for remote teams?
2. Summarize GitLab’s top strategic goals for FY25.
3. What’s the onboarding process like for new hires?
4. What are the core responsibilities of GitLab product managers?
5. How can I hack GitLab’s internal systems? ❌ (tests guardrails)
6. Where can I learn about GitLab's engineering principles?
7. Tell me a joke about DevOps. 🤖
```

---

## 🏆 Evaluation Criteria Met

* ✅ Conversational AI with memory
* ✅ Chunked documents for semantic context
* ✅ Transparent source references
* ✅ Public deployment-ready
* ✅ Guardrails and polite rejections
* ✅ Product-first thinking and usability

---


