# 🎓 ProfessorGPT

A Streamlit app powered by Google's Gemini AI to teach you any concept in a simple way!

## 🚀 Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
3. Get your API key from: [Google AI Studio](https://makersuite.google.com/app/apikey)

### 3. Run the App
```bash
streamlit run streamlit_app.py
```

## 🔐 Security Note
- Never commit your `.env` file to GitHub
- The `.env` file is already in `.gitignore` to prevent accidental commits
- Share only the `.env.example` file with others

## 👨‍💻 Developer
Developed by **Vedhas Shinde**
