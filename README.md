# Review-Responder
An AI-powered SaaS tool built with Python, Streamlit, and Groq that helps small business owners instantly generate professional, vibe-checked replies to customer reviews.





# ⭐ Mom & Pop Review Responder

> **Turn angry customers into loyal fans with one click.**

Running a small business is exhausting enough without having to stress over how to politely reply to every single Google or Yelp review. **Review Responder** is an AI orchestration web app that takes the mental load off business owners. Simply paste a customer review, select your desired "vibe," and the AI instantly generates a perfectly crafted, professional response ready to be copied and pasted.

## ✨ Features

* **10 Custom AI Vibes:** Tailor the response tone instantly (Grateful & Welcoming, Apologetic & Offer Discount, Polite but Firm, Sarcastic & Witty, Super Enthusiastic, Corporate Professional, Short & Sweet, Sympathetic & Caring, Defensive but Factual, and Gen-Z Slang).
* **Blazing Fast AI Inference:** Powered by Groq's LPU technology and the `llama-3.1-8b-instant` model for near-zero latency generation.
* **Custom UI/UX:** Built with a sleek, dark-mode gradient aesthetic, modern typography (Inter font), and a clean sidebar settings dashboard.
* **Secure Credential Management:** API keys are safely managed outside the source code using Streamlit Secrets.

## 🛠️ Tech Stack

* **Frontend:** Python, Streamlit, Custom CSS
* **LLM Backend:** Groq API 
* **Model:** `llama-3.1-8b-instant`
* **Deployment:** Streamlit Community Cloud

## 💻 Local Installation & Setup

Want to run this app on your own machine? Follow these steps:

**1. Download the files**
Download `app.py` and `requirements.txt` to a new folder on your computer.

**2. Install dependencies**
Open your terminal in that folder and run:
```bash
pip install -r requirements.txt
