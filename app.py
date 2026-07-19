import streamlit as st

st.set_page_config(
    page_title="Coisas úteis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

with open("style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown("""
<h1 class="titulo">Coisas úteis</h1>
""", unsafe_allow_html=True)

st.link_button("👥 IA's", "/ias", use_container_width=False)
    st.switch_page("pages/ias.py")

st.markdown("""
   <div class="button-container">
    <a href="https://chatgpt.com/" class="botoes">chatgpt</a>
    <a href="https://GOOGLE.COM" class="botoes">GOOGLE AI</a>
    <a href="https://lovable.dev/" class="botoes">LOVABLE</a>
   </div>
""", unsafe_allow_html=True)
