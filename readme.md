# 📊 AI Project Manager Bot

An AI-powered assistant to help project managers track updates, generate summaries, and detect blockers using OpenAI's GPT models.

---

## 🚀 Features

- ✅ Log project task updates with timestamps
- ✅ Automatically generate weekly summaries from updates
- ✅ Detect blockers or project risks from logs
- ✅ Simple CLI interface for non-technical users
- ✅ Modular and easily extendable Python architecture

---

## 📁 Project Structure

```
ai-project-manager-bot/
├── app.py
├── LICENSE
├── .env.example
├── requirements.txt
├── README.md
├── project_data.json         # Auto-created to store updates
├── utils/
│   ├── db_utils.py           # For saving & loading updates
│   └── gpt_chain.py          # GPT API interface
├── task_manager.py           # Save task updates
├── summary_generator.py      # Generate project summaries
└── blockers_analyzer.py      # Detect project risks or blockers
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-project-manager-bot.git
cd ai-project-manager-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Key

Create a `.env` file in the root directory:

```bash
touch .env
```

Paste your OpenAI key:

```ini
OPENAI_API_KEY=your_openai_key_here
```

> ⚠️ Do **not** commit `.env` to GitHub. It's already in `.gitignore`.

---

## ▶️ Run the App

```bash
python app.py
```

You'll see a menu:

```
1. Log Task Update
2. Generate Summary
3. Detect Blockers
4. Exit
```

---

## 🧠 How it Works

- All task updates are saved in `project_data.json`
- GPT-4 is used to convert raw updates into executive summaries
- Blockers are detected based on natural language analysis

---

## 📦 Example Use Case

```text
Update: "Completed frontend UI for login module"
Update: "Stuck on integrating payment gateway API due to timeout error"
```

Summary Output:
> This week, progress was made on the frontend UI. However, integration with the payment gateway faced technical issues.

Blocker Output:
> ⚠️ API timeout errors during payment integration.

---

## 🛡 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to improve.

---

## 🔥 Future Enhancements

- Web dashboard UI
- Slack / Discord / Jira integrations
- Task prioritization using LLMs

---