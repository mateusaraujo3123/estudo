import streamlit as st

st.button("IA´s")

col1, col2, col3 = st.columns(3)

with col1:
    <a href="https://chatgpt.com/" class="CHAT-GPT">
    CHAT GPT
    </a>

with col2:
    st.link_button("GOOGLE AI", "https://GOOGLE.COM")

with col3:
    st.link_button("LOVABLE", "https://lovable.dev/")
