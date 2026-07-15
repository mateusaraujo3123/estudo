import streamlit as st

st.set_page_config(
    page_title="MEU PAINEL",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def injetor_css_externo(caminho_arquivo):
    """Lê um arquivo .css puramente textual e injeta no Streamlit"""
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        # Envolve o texto do CSS puro dentro da tag <style> do HTML
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==========================================
# CÓDIGO DO CABEÇALHO (HTML + CSS)
# ==========================================
html_cabecalho = """
<div class="cabecalho-container">
    <h2 class="cabecalho-texto">🛍️ MERCADINHO Portal Da Vila</h2>
    <div class="status-online">🟢 online</div>
</div>
"""
st.markdown(html_cabecalho, unsafe_allow_html=True)

# 1. Chama o injetor apontando para o seu arquivo de estilo separado
injetor_css_externo("style.css")

# 2. Seu conteúdo do site com as classes limpas
st.markdown('<h1 class="meu-titulo">COISAS TALVEZ UTEIS</h1>', unsafe_allow_html=True)
st.markdown('<p class="meu-subtitulo">Por Matheus Araujo</p>', unsafe_allow_html=True)

st.title("IA´s")

col1, col2, col3 = st.columns(3)

with col1:
    if st.link_button("👥 FIADOS", "https://portmercado.streamlit.app/"):
        st.toast("Abrindo painel de Fiados...")

with col2:
    if st.link_button("📦 PREÇOS", "https://portmercado.streamlit.app/"):
       st.toast("Abrindo tabela de Preços...")

with col3:
    if  st.link_button("abrir contar", "https://portmercado.streamlit.app/"):
        st.toast("Abrindo Contas a Receber...")
        st.text("Abrindo Contas a Receber...")
