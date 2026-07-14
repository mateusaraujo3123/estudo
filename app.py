import streamlit as st

st.set_page_config(
    page_title="MEU PAINEL",
    layout="wide",
    initial_sidebar_state="collapsed"
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👥 FIADOS", key="btn_fiados"):
        st.toast("Abrindo painel de Fiados...")

with col2:
    if st.button("📦 PREÇOS", key="btn_precos"):
        st.toast("Abrindo tabela de Preços...")

with col3:
    if  st.link_button("abrir contar", "https://portmercado.streamlit.app/"):
        st.toast("Abrindo Contas a Receber...")
)
