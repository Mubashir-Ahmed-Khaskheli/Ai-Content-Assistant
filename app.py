import streamlit as st
from groq import Groq

# Page Configuration
st.set_page_config(page_title="AI Content Assistant", page_icon="✍️", layout="centered")

# Custom CSS for Sleek UI & Centered Bigger Header
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        color: #1E293B;
        text-align: center;
        margin-top: -10px;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #64748B;
        text-align: center;
        margin-bottom: 30px;
    }
    .content-box {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        margin-top: 15px;
        white-space: pre-wrap;
    }
    </style>
""", unsafe_allow_html=True)

# App Header (Centered & Larger)
st.markdown("<p class='main-header'>✍️ AI Content Assistant</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Generate tailored social media posts, blogs, and scripts instantly.</p>", unsafe_allow_html=True)

# Sidebar Settings
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Safe check for st.secrets
    secret_key = ""
    try:
        if "GROQ_API_KEY" in st.secrets:
            secret_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        secret_key = ""
    
    user_api_key = st.text_input(
        "Groq API Key", 
        value=secret_key, 
        type="password",
        help="Secrets se key auto-fill ho jati hai."
    )
    st.caption("Get a free key at [console.groq.com](https://console.groq.com)")
    
    st.divider()
    st.metric(label="Powered By", value="Groq LPU⚡")
    st.caption("Model: `openai/gpt-oss-120b`")

api_key = user_api_key.strip()

# Input Form
with st.form("content_form"):
    st.subheader("🎯 Content Parameters")
    col1, col2 = st.columns(2)
    
    with col1:
        content_type = st.selectbox(
            "Content Type",
            ["Social Media Post", "Blog Post", "Email Newsletter", "Ad Copy", "Video Script"]
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
        target_audience = st.text_input("Target Audience", placeholder="e.g., Software Engineers")

    submit_button = st.form_submit_button("🚀 Generate Content", use_container_width=True)

# Generation Logic
if submit_button:
    if not api_key:
        st.error("Please enter your Groq API Key in the sidebar or add GROQ_API_KEY to Secrets.")
    elif not topic or not target_audience:
        st.warning("Please fill in both Topic and Target Audience fields.")
    else:
        try:
            client = Groq(api_key=api_key)
            
            # Strict prompt to prevent excessive emojis
            prompt = f"""
            You are an expert copywriter. Generate high-quality content based on these parameters:
            - Content Type: {content_type}
            - Platform: {platform}
            - Topic: {topic}
            - Target Audience: {target_audience}
            - Tone: {tone}

            Formatting Rules:
            1. Keep the output clean, professional, and well-structured with clear line breaks.
            2. Use emojis VERY minimally and strictly where relevant (maximum 2-4 emojis in the entire response). Do NOT overload sentences with emojis.
            3. Make sure length and formatting align with best practices for {platform}.
            """

            with st.spinner("⚡ Generating high-speed content via Groq..."):
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system", 
                            "content": "You are a professional copywriter who writes concise, high-converting content with minimal and tasteful emoji usage."
                        },
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.6  # Reduced temperature slightly for more structured output
                )
            
            generated_text = response.choices[0].message.content
            
            st.success("✨ Content generated successfully!")
            
            st.subheader("📝 Output Preview")
            st.markdown(f"<div class='content-box'>{generated_text}</div>", unsafe_allow_html=True)
            
            st.write("") # spacing
            
            # Download Button
            st.download_button(
                label="📥 Download Content (.txt)",
                data=generated_text,
                file_name=f"{content_type.lower().replace(' ', '_')}_content.txt",
                mime="text/plain",
                type="primary",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")