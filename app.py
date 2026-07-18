import streamlit as st

with open("style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

st.title("Coisas úteis")

st.button("IA´s")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <a href="https://chatgpt.com/" class="botoes">
      chatgpt
    </a>
    """, unsafe_allow_html=True)
    
with col2:
    st.link_button("GOOGLE AI", "https://GOOGLE.COM")

with col3:
    st.link_button("LOVABLE", "https://lovable.dev/")
