import streamlit as st
from chatbot_model import get_answer, questions, answers

# Page setup
st.set_page_config(
    page_title="InterviewPrep AI",
    page_icon="🤖",
    layout="centered"
)

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
st.sidebar.title("🤖 InterviewPrep AI")

menu = st.sidebar.radio(
    "Menu",
    [
        "💬 Chat",
        "➕ Add New Data",
        "📝 Description",
        "📚 Question List & Answers"
    ]
)

# Clear chat
if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []

# ---------------- CHAT ----------------
if menu == "💬 Chat":

    st.title("🤖 InterviewPrep AI")
    st.caption("Smart Interview Chatbot using Transformer Embeddings")

    st.success("Welcome! Ask interview-related questions.")

    # Show history
    for msg in st.session_state.messages:

        avatar = "🧑" if msg["role"] == "user" else "🤖"

        with st.chat_message(msg["role"], avatar=avatar):
            st.write(msg["content"])

    # Chat input
    user_input = st.chat_input("Type your question here...")

    if user_input:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        with st.chat_message("user", avatar="🧑"):
            st.write(user_input)

        response = get_answer(user_input)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        with st.chat_message("assistant", avatar="🤖"):
            st.write(response)

# ---------------- ADD DATA ----------------
elif menu == "➕ Add New Data":

    st.title("➕ Add New Question & Answer")

    new_q = st.text_input("Enter Question")
    new_a = st.text_area("Enter Answer")

    if st.button("Save Data"):

        with open("questions", "a", encoding="utf-8") as f:
            f.write("\n" + new_q)

        with open("answers", "a", encoding="utf-8") as f:
            f.write("\n" + new_a)

        st.success("Data Added Successfully!")

# ---------------- DESCRIPTION ----------------
elif menu == "📝 Description":

    st.title("📝 Project Description")

    st.write("""
    InterviewPrep AI is an intelligent NLP chatbot designed for interview preparation.

    This chatbot uses Transformer-based sentence embeddings and cosine similarity to understand user questions and provide the most relevant answers from a custom question-answer dataset.

    Features:
    • Transformer Embeddings  
    • Cosine Similarity Matching  
    • Interview Question Answering  
    • Streamlit Web Interface  
    • Chat History  
    • Dynamic Dataset Support  

    Unlike keyword-based matching, the chatbot focuses on sentence meaning, which improves response accuracy and user interaction.
    """)

# ---------------- QUESTION LIST ----------------
elif menu == "📚 Question List & Answers":

    st.title("📚 Question List & Answers")

    for q, a in zip(questions, answers):
        with st.expander(q):
            st.write(a)

# Footer
st.markdown("---")
st.caption("Built with Streamlit + Transformer Embeddings")

st.markdown(
    """
    <style>
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 5px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: #9e9e9e;
        opacity: 0.8;
        z-index: 100;
        pointer-events: none;
    }
    </style>

    <div class="custom-footer">
        <div>Developed by Prachi. InterviewPrep AI can make mistakes.</div>
    </div>
    """,
    unsafe_allow_html=True
)