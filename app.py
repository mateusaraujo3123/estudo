import streamlit as st

st.set_page_config(
    page_title="Coisas úteis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

def home():
    st.markdown('<h1 class="titulo">Coisas úteis</h1>', unsafe_allow_html=True)

    st.page_link(ias, label="👥 IA's")

    st.markdown("""
    <div class="button-container">
        <a href="https://chatgpt.com/" class="botoes" target="_blank">ChatGPT</a>
        <a href="https://google.com/" class="botoes" target="_blank">Google AI</a>
        <a href="https://lovable.dev/" class="botoes" target="_blank">Lovable</a>
    </div>
    """, unsafe_allow_html=True)

home_page = st.Page(home, title="Home")
ias = st.Page("pages/ias.py", title="IA's")

st.navigation([home_page, ias], position="hidden").run()
