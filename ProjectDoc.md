# 📄 GitLab GenAI Chatbot – Project Documentation

## 🧠 Project Objective

Inspired by GitLab's “**build in public**” culture, this project implements an interactive AI-powered chatbot that enables GitLab team members and aspiring employees to explore key knowledge from the official [GitLab Handbook](https://about.gitlab.com/handbook/) and [GitLab Direction](https://about.gitlab.com/direction/) pages.

The chatbot offers accessible, conversational learning by integrating structured documentation with cutting-edge retrieval and generation techniques.

---

## 🛠️ Approach Overview

### 🔍 Step-by-Step Workflow

| **Phase**          | **Details**                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| Data Acquisition   | Handbook and Direction data was scraped/downloaded directly from GitLab’s repository and site  |
| Preprocessing      | Cleaned, section-tagged, and merged into `handbook_cleaned_FULL.txt` and `direction_final.txt` |
| Chunking           | Used `RecursiveCharacterTextSplitter` with 750/150 chunk size to preserve semantic structure   |
| Embedding          | Applied `HuggingFaceEmbeddings` with SentenceTransformer `all-MiniLM-L6-v2`                    |
| Vector Storage     | Stored using `FAISS`, persisted locally in `data/faiss_index`                                  |
| LLM Integration    | Gemini 2.5 Flash via `langchain-google-genai` for fast, responsive chat generation             |
| Retrieval Strategy | Max Marginal Relevance (MMR) to ensure diversity in context and avoid repetition               |
| Frontend           | Built with Streamlit and LangChain ConversationalRetrievalChain                                |
| Memory             | `ConversationSummaryBufferMemory` to retain long-term context and follow-ups                   |
| Guardrails         | Added ethical safety and rejection behavior for off-topic or harmful prompts                   |
| Deployment         | GitHub + Git LFS ready, compatible with Streamlit Cloud or Hugging Face Spaces                 |

---

## ⚙️ Key Technical Choices

### 1. **Data Handling & Structure**

* 📘 **Source:** Extracted from the official GitLab [Handbook Git Repo](https://gitlab.com/gitlab-com/content-sites/handbook) and Direction site.
* 🧼 Cleaned and structured into large `.txt` files with `## SECTION:` markers to preserve hierarchy.
* 🧩 Used section headers to inject metadata into chunks (improves traceability and source transparency).

### 2. **Chunking Strategy**

* 📏 `RecursiveCharacterTextSplitter`
* `chunk_size=750`, `chunk_overlap=150` – ensures semantic paragraphs aren't broken mid-thought.
* ✅ Well-suited for long-form documents like handbooks and strategy papers.

### 3. **Embedding & Retrieval**

* 🔡 Model: `all-MiniLM-L6-v2` from HuggingFace (local, privacy-safe)
* 🧠 Vector DB: `FAISS` for fast, persistent local search
* 🔁 **Retrieval method**: `MMR` (Max Marginal Relevance)

  * `k=8`, `fetch_k=18`
  * Ensures diverse, non-redundant context for better LLM outputs.

### 4. **Conversational Chain**

* LLM: `Gemini 2.5 Flash` via `langchain-google-genai`
* Chain: `ConversationalRetrievalChain` with:

  * Custom Prompt
  * `ConversationSummaryBufferMemory` for long-term context retention
  * Explicit `output_key="answer"` to avoid multi-key memory issues

### 5. **Prompt Engineering**

```text
You are an expert assistant trained on GitLab's official Handbook and Direction documents.

Please:
- Answer with as much useful detail as possible.
- Use bullet points or formatting if appropriate.
- Cite the source section when available.
- Only answer from GitLab materials. Politely decline anything off-topic.
```

---

## 💡 Innovations & Enhancements

| **Feature**                    | **Impact**                                                           |
| ------------------------------ | -------------------------------------------------------------------- |
| ✅ **MMR + Metadata Chunks**    | Improves diversity and traceability in responses                     |
| ✅ **Contextual Memory Buffer** | Retains meaningful summaries to support follow-up queries            |
| ✅ **Streamlit Spinner**        | Enhances UX by showing progress while the bot “thinks”               |
| ✅ **Transparent Citations**    | Shows users exactly which section/source was used                    |
| ✅ **Guardrails**               | Politely rejects unethical or irrelevant questions                   |
| ✅ **Git LFS Support**          | Ensures `index.faiss` (90MB+) is trackable and deployable via GitHub |
| ✅ **Production-Ready UI**      | Clean, minimalist, responsive Streamlit interface                    |

---

## 🧪 Testing & Evaluation

* Used 15+ varied test prompts (factual, contextual, follow-up, off-topic)
* Retained context across onboarding and values-related questions
* Cited source sections effectively
* Passed guardrail checks (e.g., rejecting hacking prompts)
* Fast response time with Gemini 2.5 Flash

---

## 📦 Deployment & Access

* [✅ GitHub Repo]()
* Git LFS enabled for large vector index files
* Can be deployed to:

  * [Streamlit Cloud](https://streamlit.io/cloud)
  * Hugging Face Spaces
  * Vercel (with API adaptation)

---

## 🔚 Conclusion

This project delivers a **powerful yet safe** conversational interface for navigating GitLab’s internal knowledge. It reflects GitLab’s values — transparency, asynchronous collaboration, and documentation-first culture — while showcasing production-ready GenAI engineering.


