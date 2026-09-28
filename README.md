# 🤖 AI Virtual DSA Technical Interviewer

An intelligent, multi-turn AI DSA (Data Structures & Algorithms) technical interviewer that evaluates your problem-solving, verbal communication, code correctness, and algorithmic complexity in real-time.

```
                         YOUR DSA INTERVIEWER
                                  │
                                  ▼
                           AI asks question
                                  │
                      ┌───────────┴───────────┐
                      ▼                       ▼
                🎤 Your Voice             ⌨️ Your Code
                      │                       │
                      ▼                       │
               Speech-to-Text                 │
                      │                       │
                      └───────────┬───────────┘
                                  ▼
                           LangChain Prompt
                                  │
                                  ▼
                             GPT-4o Model
                                  │
                       ┌──────────┼──────────┐
                       ▼          ▼          ▼
                      Good       Hint     Correction
                       │          │          │
                       └──────────┼──────────┘
                                  ▼
                           AI Voice Response
```

---

## 🌟 Key Features

1. **🎤 Microphone & Whisper Speech-to-Text (STT)**:
   - Speak your thought process and problem approach naturally.
   - Live transcription powered by OpenAI Whisper (`whisper-1`).
   - Seamless interactive text fallback if microphone is unavailable.

2. **⌨️ Interactive In-Terminal Java Code Editor**:
   - Multi-line Java code editor with syntax highlighting powered by `prompt_toolkit` and `pygments`.
   - Preloaded starter code and method signatures.
   - Quick external editor support (`:editor` launches Notepad, VS Code, or Vim).

3. **🔊 AI Voice Response (TTS)**:
   - Natural spoken responses from the AI interviewer via OpenAI TTS (`tts-1`).
   - Multiple interviewer voices (`alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`).

4. **🧠 LangGraph Multi-Turn State Machine**:
   - Full contextual memory of previous turns, code versions, and explanations.
   - **Progressive Socratic Hints**:
     - *Mistake #1* ➔ **Hint #1** (subtle conceptual clue).
     - *Mistake #2* ➔ **Hint #2** (targeted structural guidance).
   - **Complexity Interrogation**: Follow-up check for Time and Space Complexity ($O(N)$, $O(1)$, etc.).
   - **Multi-Question Progression**: Advances to Question 2, Question 3, etc.
   - **Final Performance Scorecard**: Detailed rubric report (Score /10, Strengths, Weaknesses, Complexity, Next Steps).

---

## 🔁 LangGraph Interview Flow

```
Question 1 (AI Voice + Display)
   │
   ▼
Your Spoken Explanation (🎤 Mic / STT)
   │
   ▼
Your Java Code (⌨️ Terminal Editor)
   │
   ▼
AI Evaluator (GPT-4o)
   │
   ├── [Mistake Found] ──> Hint #1 ──> Your Correction ──> Evaluator
   │                                                             │
   │                                                       [Still Stuck]
   │                                                             │
   │                                                             ▼
   │                                                          Hint #2
   │
   └── [Code Correct] ──> Complexity Question (Time & Space O(N))
                               │
                               ▼
                          Question 2
                               │
                               ▼
                       Final Scorecard & Report
```

---

## 🚀 Getting Started

### 1. Prerequisites & Installation

Ensure you have Python 3.11+ and `uv` installed.

```bash
# Install dependencies with uv
uv sync
```

### 2. Configure OpenAI API Key

Create or update your `.env` file in the project root:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
```

### 3. Launch the Application

#### 🌐 Option A: Launch Interactive Streamlit Web UI (Recommended)
```bash
# Launch the Streamlit Web Application
streamlit run app.py

# Or via CLI flag
python src/ai_interviewer/dsa_interviewer.py --ui
```

#### 💻 Option B: Run in Terminal
```bash
# Start a full voice & code interview in terminal
python src/ai_interviewer/dsa_interviewer.py

# Or run via installed command
ai-interviewer
```


---

## ⚙️ CLI Options & Customization

| Flag | Description | Example |
| :--- | :--- | :--- |
| `-q`, `--questions` | Number of questions in interview (default: `2`) | `python src/ai_interviewer/dsa_interviewer.py -q 3` |
| `-t`, `--topic` | Filter by DSA topic (`Strings`, `Arrays`, `Stack`, `DP`, etc.) | `python src/ai_interviewer/dsa_interviewer.py -t "Strings"` |
| `--no-mic` | Use keyboard typing instead of microphone STT | `python src/ai_interviewer/dsa_interviewer.py --no-mic` |
| `--no-voice` | Disable AI Voice audio output (text-only mode) | `python src/ai_interviewer/dsa_interviewer.py --no-voice` |
| `--voice` | OpenAI TTS voice persona (`alloy`, `nova`, `echo`, etc.) | `python src/ai_interviewer/dsa_interviewer.py --voice nova` |
| `--model` | OpenAI evaluation model (default: `gpt-4o`) | `python src/ai_interviewer/dsa_interviewer.py --model gpt-4o` |

---

## 📁 Project Architecture

```
AI_Interviewer/
├── src/
│   └── ai_interviewer/
│       ├── __init__.py          # Package exports & main entrypoint
│       ├── audio.py             # Audio recorder, Whisper STT & OpenAI TTS
│       ├── editor.py            # In-terminal Java code editor
│       ├── prompts.py           # Evaluation, Hint & Scorecard LLM prompts
│       ├── questions.py         # Curated DSA question bank
│       ├── state.py             # LangGraph state & transcript models
│       ├── graph.py             # LangGraph multi-turn state machine
│       └── dsa_interviewer.py   # CLI entry point & UI orchestration
├── pyproject.toml               # Project metadata & dependencies
├── requirements.txt             # Pip dependencies
└── README.md                    # Documentation
```
