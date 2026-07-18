import streamlit as st

st.button("IA´s")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("CHAT GPT", "https://chatgpt.com/")

with col2:
    st.link_button("GOOGLE AI", "https://GOOGLE.COM")

with col3:
    st.link_button("LOVABLE", "https://lovable.dev/")
