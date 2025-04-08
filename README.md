# ai-agent

AI Agent powered by **LangChain**, using **Gemini (Google Generative AI) LLM**, and smart tools.  

Features include:

-  Conversational memory
-  Retrieval-Augmented Generation (RAG)
-  Time-aware responses
-  Secure terminal command generation (with approval)
-  DuckDuckGo web search tool

---

## 🚀 Getting Started


### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-agent.git
cd ai-agent
```


### 2. Install requirements



- ### Option a: Use existing requirements.txt 

- Make sure you’re using Python 3.10+.

 ```bash
 pip install -r requirements.txt
 ```



- ### Option b: Generate `requirements.txt` (for advanced users)

- If you want to regenerate `requirements.txt` from actual imports in the project:

- #### a. Install pipreqs

```bash
pip install pipreqs
```

- #### b. Navigate to your project folder

```bash
cd path/to/your/project
```

- #### c. Generate `requirements.txt`

```bash
pipreqs . --force
```

- #### d. Install the generated dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Add your API key

Create a `.env` file in the project root:

```
GEMINI_KEY=your_google_api_key_here
```

---

## How It Works

1. Loads your personal files into a vectorstore (via FAISS)
2. Initializes a LangChain agent with:
   - Google Gemini model
   - Memory
   - RAG tool
   - Terminal command generator
   - Time + Web Search tools
3. Starts a loop where you can ask questions or give instructions

---

## 🧩 Project Structure

```bash
.
├── app.py                  # Main entrypoint: launches the agent loop
├── agent_factory.py        # Builds LangChain agent with tools
├── chain_factory.py        # Creates RAG-aware chains
├── config.py               # Model settings and session ID
├── executor.py             # Executes shell commands safely
├── load_docs.py            # Loads files and creates vectorstore
├── memory.py               # Manages in-session memory
├── tools.py                # Time, search, command, RAG tools
├── .env                    # Gemini API key
├── .gitignore
```

---

## 🛠️ Tools Used

| Tool Name                    | Description                                      |
|-----------------------------|--------------------------------------------------|
| `get_current_time`          | Returns the current date/time                   |
| `search`                    | Web search using DuckDuckGo                     |
| `create_terminal_command`   | Suggests terminal commands                      |
| `retrieval_augmented_generation` | RAG: searches your documents            |

---

## 🧪 Example

```bash
$ python app.py

You: What's the current time?
AI: 2025-04-07 11:05:23

You: Remove node_modules folder
AI wants to run: rm -rf node_modules
Approve? (y/n): n
Command execution cancelled.
```

---

## 📁 Add Custom Documents

You can place your `.txt` files in the project and update:

```python
vectorstore = load_vectorstore(files, api_key)
```

to include your own docs. They will then be searchable using the RAG tool.

---

## 💾 Memory

- Stored in memory during runtime using `ChatMessageHistory`
- Saved to `chat_history.txt` when you exit

---

## 📜 License

MIT License.  
You must visit Google Gemini API usage rules: https://ai.google.dev/terms

---

## 🧾 Requirements

```txt
duckduckgo_search==7.5.5
langchain==0.3.23
langchain_community==0.3.21
langchain_core==0.3.51
langchain_google_genai==2.1.2
matplotlib==3.10.1
numpy==2.2.4
protobuf==6.30.2
python-dotenv==1.1.0
scikit_learn==1.6.1
sentence_transformers==4.0.1
umap_learn==0.5.7
```

---
