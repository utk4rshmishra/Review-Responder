import streamlit as st
from groq import Groq

# 1. PAGE CONFIG (This adds an icon to your actual browser tab!)
st.set_page_config(page_title="Review Responder", page_icon="⭐", layout="centered")

# 2. KEEP THE CLASSY CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    div.stButton > button {
        background-color: #1E90FF; color: white; border-radius: 8px; border: none; padding: 10px 24px; font-weight: 600; width: 100%; transition: all 0.3s ease;
    }
    div.stButton > button:hover { background-color: #00BFFF; transform: translateY(-2px); }
</style>
""", unsafe_allow_html=True)

# 3. DASHBOARD SIDEBAR (Pro tools use sidebars for settings)
with st.sidebar:
    st.header("⚙️ Response Settings")
    st.write("Customize how the AI talks to your customers.")
    
    # Notice the icons added directly to the text!
    vibe = st.selectbox("Select the Vibe:", [
        "🤝 Grateful & Welcoming",
        "💸 Apologetic & Offer Discount",
        "🛡️ Polite but Firm",
        "😏 Sarcastic & Witty",
        "🎉 Super Enthusiastic",
        "👔 Corporate Professional",
        "⚡ Short & Sweet",
        "❤️ Sympathetic & Caring",
        "✋ Defensive but Factual",
        "📱 Gen-Z Slang"
    ])

# 4. MAIN DASHBOARD AREA
st.title("⭐ Mom & Pop Review Responder")
st.write("Turn angry customers into loyal fans with one click. Paste a review below.")

# Text area with a helpful placeholder
review = st.text_area("👇 Customer Review:", height=150, placeholder="e.g., 'The food was cold and the waiter was rude!'")

# 5. THE BUTTON & AI LOGIC
if st.button("🚀 Generate Professional Reply"):
    if review:
        with st.spinner("Brainstorming the perfect reply... 🧠"):
            # Call the Groq AI
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            prompt = f"You are a professional small business owner. Write a short, polite reply to the following customer review. Ensure the tone matches this specific vibe: {vibe}. Here is the review: {review}"
            
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.1-8b-instant",
            )
            
            # 6. BEAUTIFUL OUTPUT DISPLAY
            st.success("✨ Here is your perfect reply:")
            # st.info creates a nice, colored callout box for the result
            st.info(response.choices[0].message.content)
            
    else:
        st.warning("⚠️ Please paste a review first!")