# ✂️ LangChain Text Splitters

> *Exploring 4 different strategies to split text into meaningful chunks — from simple character-based to intelligent semantic splitting.*

---

## 📂 Project Structure

```
LangChainTextSplitter/
├── lengthbased_splitter.py               # 📏 Fixed-size character splitting
├── text_structure_based_splitter.py      # 🔁 Recursive splitting by text structure
├── doc_struct_based_splitter.py          # 🧬 Language-aware code splitting
├── semantic_meaning_based_splittter.py   # 🧠 Embedding-powered semantic chunking
└── README.md
```

---

## 📖 Splitter Breakdown

### 1️⃣ Length-Based Splitter — `lengthbased_splitter.py`

> Splits text into fixed-size chunks based on **character count** — the simplest approach.

| Detail | Value |
|--------|-------|
| **Splitter** | `CharacterTextSplitter` |
| **Chunk Size** | 100 characters |
| **Chunk Overlap** | 0 |
| **Separator** | Empty string (split anywhere) |
| **Data Source** | Web article via `WebBaseLoader` |

**How it works:** The text is sliced into uniform chunks of a specified size — no awareness of sentence boundaries, paragraphs, or meaning. Fast and predictable, but may cut mid-sentence.

```python
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

loader = WebBaseLoader("https://www.journalofdemocracy.org/articles/why-gen-z-is-rising/")
docs = loader.load()
chunks = splitter.split_documents(docs)
```

> 💡 **Best for:** Quick prototyping or when uniform chunk sizes matter more than content coherence.

---

### 2️⃣ Text Structure-Based Splitter — `text_structure_based_splitter.py`

> Uses **recursive splitting** to intelligently break text along natural boundaries — paragraphs, then sentences, then words.

| Detail | Value |
|--------|-------|
| **Splitter** | `RecursiveCharacterTextSplitter` |
| **Chunk Size** | 100 characters |
| **Chunk Overlap** | 0 |
| **Separators (default)** | `\n\n` → `\n` → ` ` → `""` |

**How it works:** Instead of blindly cutting at a fixed length, it tries the most natural split point first (`\n\n` for paragraphs), then falls back to smaller boundaries (`\n`, then spaces) if the chunk is still too large. This preserves sentence and paragraph integrity wherever possible.

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
```

> 💡 **Best for:** General-purpose text splitting — the **recommended default** for most use cases.

---

### 3️⃣ Document Structure-Based Splitter — `doc_struct_based_splitter.py`

> **Language-aware splitting** for source code — respects the syntax and structure of programming languages.

| Detail | Value |
|--------|-------|
| **Splitter** | `RecursiveCharacterTextSplitter.from_language()` |
| **Language** | Python |
| **Chunk Size** | 300 characters |
| **Chunk Overlap** | 0 |
| **Separators** | Language-specific (class, function, etc.) |

**How it works:** Uses language-specific separators to split code at meaningful structural boundaries — class definitions, function definitions, and logical blocks — instead of arbitrary character positions. Supports 15+ languages including Python, JavaScript, Go, Java, and more.

```python
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(code)
```

**Supported languages include:**

| | | | |
|--|--|--|--|
| 🐍 Python | ☕ Java | 🟨 JavaScript | 🦀 Rust |
| 🔵 Go | 💎 Ruby | ⚡ C/C++ | 📝 Markdown |

> 💡 **Best for:** Splitting source code for code-aware RAG pipelines, documentation generation, or code analysis.

---

### 4️⃣ Semantic Meaning-Based Splitter — `semantic_meaning_based_splittter.py`

> The most intelligent approach — uses **embeddings to detect topic shifts** and splits at semantic boundaries.

| Detail | Value |
|--------|-------|
| **Splitter** | `SemanticChunker` (experimental) |
| **Embeddings** | Google Gemini (`gemini-embedding-2-preview`) |
| **Breakpoint Type** | Standard Deviation |
| **Threshold** | `0.2` |
| **Package** | `langchain-experimental` |

**How it works:** Each sentence is embedded into a vector. The cosine distance between consecutive sentence embeddings is computed — when the distance exceeds a threshold (i.e., the topic shifts), a new chunk boundary is created. This means chunks are **variable-length** and **content-aware**.

```python
embedding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2-preview')

splitter = SemanticChunker(
    embedding,
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=0.2
)

chunks = splitter.split_text(text)
```

**Breakpoint strategies:**

| Strategy | How it Splits |
|----------|---------------|
| `percentile` | Splits at distances above a percentile threshold |
| `standard_deviation` | Splits when distance exceeds X standard deviations from mean |
| `interquartile` | Splits at outlier distances using IQR method |

> 💡 **Best for:** High-quality RAG applications where preserving topical coherence within chunks is critical.

---

## 🔄 Comparison at a Glance

| Splitter | Awareness | Needs Embeddings? | Chunk Size | Best For |
|----------|:---------:|:-----------------:|:----------:|----------|
| **Length-Based** | ❌ None | ❌ | Fixed | Quick & simple splitting |
| **Text Structure** | 📝 Paragraphs/Sentences | ❌ | ~Fixed | General purpose (recommended) |
| **Doc Structure** | 🧬 Code syntax | ❌ | ~Fixed | Source code splitting |
| **Semantic** | 🧠 Topic/meaning | ✅ | Variable | High-quality topic-aware chunking |

```
Intelligence Level:

Length-Based  ──▶  Text Structure  ──▶  Doc Structure  ──▶  Semantic
   (naive)         (structural)        (syntax-aware)      (meaning-aware)
```

---

## 🛠️ Installation

```bash
# Core
pip install langchain langchain-text-splitters langchain-community

# Semantic Splitting
pip install langchain-experimental langchain-google-genai

# Web Loading
pip install beautifulsoup4

# Environment
pip install python-dotenv
```

> 💡 Don't forget to set up your `.env` file with your API key:
> ```env
> GOOGLE_API_KEY=your_google_api_key
> ```

---

## ▶️ Usage

```bash
# Activate virtual environment
source venv/bin/activate

# Run any splitter
python lengthbased_splitter.py
python text_structure_based_splitter.py
python doc_struct_based_splitter.py
python semantic_meaning_based_splittter.py
```

---

<p align="center">
  Built with 🦜🔗 <strong>LangChain</strong> | Embeddings by <strong>Google Gemini</strong>
</p>
