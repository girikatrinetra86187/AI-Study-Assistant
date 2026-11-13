
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load API key
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="centered"
)

# Website heading
st.title("📚 AI Study Assistant")
st.write("Your personal AI-powered learning partner!")

st.divider()

# Connect to Groq
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Groq API key not found. Check your .env file.")
    st.stop()

client = Groq(api_key=api_key)


# Generate AI response
def generate_answer(prompt):

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful study assistant. Explain everything in simple English."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=1500
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"AI Error: {error}"


# Sidebar
st.sidebar.title("Study Menu")

option = st.sidebar.selectbox(
    "Choose a feature",
    [
        "Ask AI",
        "Summarize Notes",
        "Explain a Topic",
        "Generate Quiz"
    ]
)


# FEATURE 1: ASK AI
if option == "Ask AI":

    st.header("💬 Ask AI")

    question = st.text_area(
        "Enter your question",
        placeholder="What is Artificial Intelligence?"
    )

    if st.button("Get Answer"):

        if question.strip():

            with st.spinner("AI is thinking..."):
                answer = generate_answer(question)

            st.subheader("AI Answer")
            st.markdown(answer)

        else:
            st.warning("Please enter a question.")


# FEATURE 2: SUMMARIZE NOTES
elif option == "Summarize Notes":

    st.header("📝 Summarize Study Notes")

    notes = st.text_area(
        "Paste your study notes here",
        height=200
    )

    if st.button("Summarize Notes"):

        if notes.strip():

            prompt = f"""
            Summarize these study notes in simple English.
            Include headings and important bullet points.

            Notes:
            {notes}
            """

            with st.spinner("Preparing summary..."):
                answer = generate_answer(prompt)

            st.subheader("Your Summary")
            st.markdown(answer)

        else:
            st.warning("Please paste your notes.")


# FEATURE 3: EXPLAIN A TOPIC
elif option == "Explain a Topic":

    st.header("📖 Understand Difficult Topics")

    topic = st.text_input(
        "Enter a topic",
        placeholder="Example: Python Programming"
    )

    if st.button("Explain"):

        if topic.strip():

            prompt = f"""
            Explain {topic} in simple English.

            Include:
            1. Definition
            2. Important points
            3. Real-life example
            4. Advantages
            5. Short conclusion
            """

            with st.spinner("Explaining the topic..."):
                answer = generate_answer(prompt)

            st.subheader("Topic Explanation")
            st.markdown(answer)

        else:
            st.warning("Please enter a topic.")


# FEATURE 4: GENERATE QUIZ
elif option == "Generate Quiz":

    st.header("🧠 Generate Your Quiz")

    subject = st.text_input(
        "Enter subject or topic",
        placeholder="Example: Python Programming"
    )

    number = st.selectbox(
        "Number of questions",
        [5, 10, 15]
    )

    if st.button("Generate Quiz"):

        if subject.strip():

            prompt = f"""
            Create {number} multiple-choice questions
            about {subject}.

            Give four options for every question.
            Show the correct answer and explain it briefly.

            Use simple English.
            """

            with st.spinner("Generating quiz..."):
                answer = generate_answer(prompt)

            st.subheader("Your AI Quiz")
            st.markdown(answer)

        else:
            st.warning("Please enter a subject.")


# Footer
st.divider()

st.caption(
    "AI Study Assistant | Python + Streamlit + Groq AI"
)
