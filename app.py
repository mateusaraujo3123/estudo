import streamlit as st

st.set_page_config(
    page_title="MEU PAINEL",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# carregar o css da pagina style
def local_css(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Aplica o estilo do arquivo separado
local_css("style.css")

col1, col2, col3 = st.columns(3)

with col1:
    if st.link_button("👥 FIADOS"):
        st.toast("Abrindo painel de Fiados...")

with col2:
    if st.link_button("📦 PREÇOS"):
        st.toast("Abrindo tabela de Preços...")

with col3:
    if  st.link_button("abrir contar", "https://portmercado.streamlit.app/"):
        st.toast("Abrindo Contas a Receber...")
        st.text("Abrindo Contas a Receber...")
