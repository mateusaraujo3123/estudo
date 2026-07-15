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
    <h2 class="cabecalho-texto"> COISAS TALVEZ UTEIS</h2>
    <div class="status-online">🟢 POR MATEUS ARAUJO</div>
</div>
"""
st.markdown(html_cabecalho, unsafe_allow_html=True)

# 1. Chama o injetor apontando para o seu arquivo de estilo separado
injetor_css_externo("style.css")

# 2. Seu conteúdo do site com as classes limpas
st.markdown('<h1 class="meu-titulo">IA´S</h1>', unsafe_allow_html=True)
st.markdown('<p class="meu-subtitulo">INTELIGÊNCIA ARTIFICIAL</p>', unsafe_allow_html=True)

if st.toast("Bem Vindo"):

col1, col2, col3 = st.columns(3)

with col1:
    if st.link_button("CHAT GPT", "https://portmercado.streamlit.app/"):

with col2:
    if st.link_button("GOOGLE AI", "https://portmercado.streamlit.app/"):

with col3:
    if  st.link_button("LOVABLE", "https://portmercado.streamlit.app/"):

st.markdown('<h1 class="meu-titulo">IA´S</h1>', unsafe_allow_html=True)
st.markdown('<p class="meu-subtitulo">INTELIGÊNCIA ARTIFICIAL</p>', unsafe_allow_html=True)
