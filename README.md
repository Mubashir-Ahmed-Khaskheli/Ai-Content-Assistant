# ✍️ AI Content Assistant

A lightweight, high-performance Streamlit web application designed to generate tailored multi-platform copy using Groq's fast LLM inference engine (`openai/gpt-oss-120b`).

---

## ✨ Key Features

* **Targeted Content Generation:** Create content for Blog Posts, Social Media Posts, Email Newsletters, Ad Copy, and Video Scripts.
* **Platform-Optimized Output:** Tailor copy structure and length specifically for LinkedIn, Twitter/X, Instagram, Facebook, Medium, or Email.
* **Custom Audience & Tone:** Fine-tune messaging based on chosen tone (Professional, Casual, Persuasive, Informative, Humorous, Witty) and specific audience demographics.
* **Dual API Key Authentication:** Supports automatic retrieval via Streamlit Secrets for cloud deployments alongside an interactive sidebar key input for local/guest users.
* **One-Click Export:** Download generated text directly as a clean `.txt` file formatted with the content type.

---

## 🛠️ Tech Stack

* **UI Framework:** [Streamlit](https://streamlit.io/?utm_source=gemini)
* **Inference Engine:** [Groq Cloud SDK](https://console.groq.com?utm_source=gemini)
* **Model:** `openai/gpt-oss-120b`
* **Language:** Python 3.9+

---

## 📁 Repository Structure

```text
.
├── app.py              # Core Streamlit UI & Groq integration logic
├── requirements.txt    # Application dependencies (streamlit, groq)
└── README.md           # Project documentation

```

---

## 🚀 Local Installation & Setup

### 1. Prerequisites

* Python 3.9 or higher installed on your system.
* A free Groq API Key from [Groq Console](https://console.groq.com?utm_source=gemini).

### 2. Clone the Repository

```bash
git clone https://github.com/Mubashir-Ahmed-Khaskheli/Ai-Content-Assistant.git
cd Ai-Content-Assistant

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the Application

```bash
streamlit run app.py

```

---

## ☁️ Streamlit Cloud Deployment

1. Push your code to GitHub.
2. Sign in to [Streamlit Cloud](https://share.streamlit.io/?utm_source=gemini).
3. Click **New app**, choose your repository (`Ai-Content-Assistant`), branch (`main`), and set the main file path to `app.py`.
4. In **Advanced Settings > Secrets**, add your Groq API key:
```toml
GROQ_API_KEY = "gsk_your_actual_api_key_here"

```


5. Click **Deploy**.

---

## 📜 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE&utm_source=gemini).
