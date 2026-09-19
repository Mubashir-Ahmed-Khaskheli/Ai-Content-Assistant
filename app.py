import streamlit as st
from groq import Groq

# Page Configuration
st.set_page_config(page_title="AI Content Assistant", page_icon="✍️", layout="centered")

st.title("✍️ AI Content Assistant")
st.write("Generate tailored content for social media, blogs, emails, and more.")

# API Key handling: Direct Streamlit Cloud secrets se uthayega, na hone par sidebar dikhayega
api_key = None

if "GROQ_API_KEY" in st.secrets:
    api_key = st.secrets["GROQ_API_KEY"]
else:
    with st.sidebar:
        st.header("Settings")
        api_key = st.text_input("Enter Groq API Key", type="password")
        st.caption("Get a free key at [console.groq.com](https://console.groq.com)")

# Input Form
with st.form("content_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        content_type = st.selectbox(
            "Content Type",
            ["Blog Post", "Social Media Post", "Email Newsletter", "Ad Copy", "Video Script"]
        )
        platform = st.selectbox(
            "Platform",
            ["LinkedIn", "Twitter/X", "Instagram", "Facebook", "Medium", "Email"]
        )
        tone = st.selectbox(
            "Tone",
            ["Professional", "Casual", "Persuasive", "Informative", "Humorous", "Witty"]
        )

    with col2:
        topic = st.text_input("Topic / Main Idea", placeholder="e.g., Remote Work Productivity")
        target_audience = st.text_input("Target Audience", placeholder="e.g., Software Engineers, Marketing Managers")

    submit_button = st.form_submit_button("Generate Content")

# Generation Logic
if submit_button:
    if not api_key:
        st.error("Please provide a Groq API key in the sidebar or via Streamlit Secrets.")
    elif not topic or not target_audience:
        st.warning("Please fill in both the Topic and Target Audience fields.")
    else:
        try:
            client = Groq(api_key=api_key)
            
            prompt = f"""
            You are an expert content creator. Generate a high-quality piece of content based on these inputs:
            - Content Type: {content_type}
            - Platform: {platform}
            - Topic: {topic}
            - Target Audience: {target_audience}
            - Tone: {tone}

            Make sure the format and length suit the specified platform perfectly.
            """

            with st.spinner("Generating content..."):
                response = client.chat.completions.create(
                    model="llama3-70b-8192",  # Updated working Groq model
                    messages=[
                        {"role": "system", "content": "You are a helpful and professional copywriter."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
            
            generated_text = response.choices[0].message.content
            
            st.success("Content Generated!")
            st.markdown("### Generated Content")
            st.write(generated_text)
            
            # Download Button
            st.download_button(
                label="📥 Download Content (.txt)",
                data=generated_text,
                file_name=f"{content_type.lower().replace(' ', '_')}_content.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")