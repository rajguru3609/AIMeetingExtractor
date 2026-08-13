
# 🎙️ AIExtractor

Turn meeting recordings into actionable insights with AI.

AIExtractor is an AI-powered meeting assistant that converts recorded meeting audio into a transcript and automatically extracts summaries, key points, action items, decisions, and follow-up emails.

---

## ✨ Features

- 🎙️ **Audio Upload** — Upload recorded meeting audio
- 📝 **Speech-to-Text** — Transcribe meetings using Whisper
- 🧠 **AI Analysis** — Analyze transcripts using Google Gemini
- 📌 **Key Points** — Extract important topics and discussions
- ✅ **Action Items** — Identify tasks and responsibilities
- 🤝 **Decisions** — Extract decisions made during meetings
- 📧 **Follow-up Email** — Generate a professional follow-up email
- 🌐 **REST API** — Flask backend for frontend integration
- 🔗 **CORS Support** — Ready for frontend-backend communication

---

## 🏗️ How It Works

```text
┌──────────────────┐
│   Meeting Audio  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│      Whisper     │
│  Speech-to-Text  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│     Transcript   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   Google Gemini  │
│   AI Analysis    │
└────────┬─────────┘
         │
         ▼
┌──────────────────────────┐
│     Meeting Insights     │
│                          │
│  • Summary               │
│  • Key Points            │
│  • Action Items          │
│  • Decisions             │
│  • Follow-up Email       │
└──────────────────────────┘

```

---

## 🛠️ Tech Stack

| Technology | Purpose |
| --- | --- |
| 🐍 **Python** | Backend language |
| 🌐 **Flask** | REST API |
| 🎙️ **Whisper** | Audio transcription |
| 🤖 **Google Gemini** | Meeting analysis |
| 🔗 **Flask-CORS** | Cross-origin requests |
| 🔐 **python-dotenv** | Environment variables |

---

## 📁 Project Structure

```text
AIExtractor/
│
├── backend/
│   ├── env/
│   ├── app.py
│   ├── gpt_utils.py
│   ├── requirements.txt
│   ├── .env
│   └── ...
│
├── frontend/
│   └── ...
│
├── .gitignore
└── README.md

```

> ⚠️ `env/` and `.env` should not be committed to GitHub.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd AIExtractor

```

### 2. Navigate to the Backend

```bash
cd backend

```

### 3. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv env

```

### 4. Activate the Virtual Environment

```powershell
.\env\Scripts\Activate.ps1

```

After activation, you should see:

```text
(env) PS C:\...\AIExtractor\backend>

```

### 5. Install Dependencies

If `requirements.txt` exists:

```bash
python -m pip install -r requirements.txt

```

Otherwise:

```bash
python -m pip install flask flask-cors python-dotenv openai-whisper google-genai

```

---

## 🔑 Environment Variables

Create a `.env` file inside the `backend` directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here

```

Your project loads the API key using `python-dotenv`.

> ⚠️ **Important:** Never commit your API key to GitHub.

Add the following to `.gitignore`:

```text
.env
env/
__pycache__/
*.pyc

```

---

## ▶️ Run the Backend

Activate the environment:

```powershell
.\env\Scripts\Activate.ps1

```

Start Flask:

```bash
python app.py

```

The API should be available at: `http://127.0.0.1:5000`

---

## 📡 API

### `POST /upload`

Uploads a meeting audio file and processes it using Whisper and Gemini.

#### Request

The endpoint expects a `multipart/form-data` request containing the audio file.

**Example:**

```bash
curl -X POST [http://127.0.0.1:5000/upload](http://127.0.0.1:5000/upload) \
  -F "file=@meeting.mp3"

```

#### Processing Pipeline

```text
Audio File
    ↓
Flask /upload
    ↓
Whisper Transcription
    ↓
Meeting Transcript
    ↓
Google Gemini
    ↓
AI-Generated Insights
    ↓
JSON / Response

```

---

## 🧠 AI Output

AIExtractor analyzes the meeting transcript and generates:

* 📋 **Summary:** A concise overview of the meeting.
* 🔑 **Key Points:** The most important topics and information discussed.
* ✅ **Action Items:** Tasks identified from the conversation, including responsible people when available.
* 🤝 **Decisions:** Important decisions and conclusions made during the meeting.
* 📧 **Follow-up Email:** A professional email summarizing the meeting and next steps.

---

## ⚡ Whisper & CPU

If Whisper is running on a CPU, you may see:

```text
UserWarning: FP16 is not supported on CPU; using FP32 instead

```

This is not an error. Whisper automatically switches from FP16 to FP32 when running without a supported GPU. A GPU can significantly improve transcription speed for larger recordings.

---

## 🐛 Troubleshooting

### Flask cannot be imported

Make sure the virtual environment is active:

```powershell
.\env\Scripts\Activate.ps1

```

Then install dependencies:

```bash
python -m pip install -r requirements.txt

```

### VS Code cannot find the virtual environment

1. Open the Command Palette: `Ctrl + Shift + P`
2. Select: `Python: Select Interpreter`
3. Choose: `backend\env\Scripts\python.exe`
4. If it doesn't appear automatically, select: `Enter interpreter path...` and manually select `env\Scripts\python.exe`

### Check which Python is being used

Run:

```bash
python -c "import sys; print(sys.executable)"

```

It should point to:
`...\AIExtractor\backend\env\Scripts\python.exe`

### Gemini API Error

Make sure your `.env` file contains:

```env
GEMINI_API_KEY=your_api_key_here

```

Also make sure the Gemini model configured in `gpt_utils.py` is currently available to your API account.

---

## 🔐 Security

Never expose API keys in:

* GitHub repositories
* Frontend code
* Public screenshots
* `.py` files
* Client-side JavaScript

Use environment variables instead:

```env
GEMINI_API_KEY=your_api_key

```

And add `.env` to `.gitignore`.

---

## 🔮 Future Improvements

* [ ] Structured JSON output
* [ ] Speaker identification
* [ ] Speaker diarization
* [ ] Support for additional audio formats
* [ ] Meeting history
* [ ] Database integration
* [ ] User authentication
* [ ] Downloadable meeting reports
* [ ] Automatic email sending
* [ ] Due-date extraction
* [ ] Frontend dashboard
* [ ] Background processing for long recordings
* [ ] GPU acceleration
* [ ] Docker support
* [ ] Cloud deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Test your changes
5. Commit your changes (`git commit -m "Add your feature"`)
6. Push the branch (`git push origin feature/your-feature`)
7. Open a Pull Request

---

## 📄 License

This project is currently intended for educational and development purposes.

Add a license such as MIT if you plan to distribute the project publicly.

---

### 👨‍💻 AIExtractor

Transforming meeting recordings into actionable intelligence.

```text
🎙️ Audio ──> 📝 Transcription ──> 🤖 AI Analysis ──> 📊 Meeting Insights ──> ✅ Actionable Results

```

*Built with Python, Flask, Whisper, and Google Gemini.*
