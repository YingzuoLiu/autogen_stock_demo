# Autogen Stock Demo (2-Agent Simplified Version)

This project uses Autogen with only two agents:
- UserProxyAgent (user)
- AssistantAgent (LLM + Code Execution)

It allows users to query and visualize stock data (e.g., from Yahoo Finance) using natural language. The assistant generates Python code and executes it to return charts.

---

## 🧠 Architecture

```
[UserProxyAgent] → [AssistantAgent]
```

The assistant both understands the user's intent and executes Python code directly.

---

## 💻 Usage

```bash
pip install -r requirements.txt
python main.py
```

Example:

```
获取今天微软的股票数据并画图
```

---

## 📁 Files

- `main.py`: Launches the 2-agent interaction
- `prompts/stock_prompt.txt`: Prompt template for future LLMs
- `requirements.txt`: Dependencies
- `README.md`: Overview

---

## 🔮 Next Steps

- Replace OpenAI with local HuggingFace GPT2 model
- Add frontend with Streamlit
- Extend to multiple stocks or comparison plots
