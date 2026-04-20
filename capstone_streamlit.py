import streamlit as st
from ecommerce_assistant.graph import app

st.title("E-commerce FAQ Bot")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "user_1"

user_input = st.text_input("Ask your question")

if st.button("Send"):
    result = app.invoke(
        {"question": user_input},
        config={"configurable": {"thread_id": st.session_state.thread_id}}
    )

    st.write("Bot:", result["answer"])