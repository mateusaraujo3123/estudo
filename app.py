import streamlit as st
import os  # Essencial: Corrigido o erro importando o módulo que faltava

st.set_page_config(
    page_title="MEU PAINEL",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def injetor_css_externo(nome_arquivo):
    """Encontra e lê o arquivo CSS no servidor de hospedagem do Streamlit"""
    # Encontra o caminho da pasta onde o script app.py está rodando
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(diretorio_atual, nome_arquivo)
    
    with open(caminho_completo, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 1. Carrega o arquivo style.css que está na mesma pasta do GitHub
injetor_css_externo("style.css")

# ==========================================
# CÓDIGO DO CABEÇALHO (HTML + CSS)
# ==========================================
html_cabecalho = """
<div class="cabecalho-container">
    <h2 class="cabecalho-texto"> COISAS TALVEZ ÚTEIS</h2>
    <div class="status-online">🟢 POR MATEUS ARAUJO</div>
</div>
"""
st.markdown(html_cabecalho, unsafe_allow_html=True)

# 2. Seu conteúdo do site com as classes limpas
st.markdown('<h1 class="meu-titulo">IA´S</h1>', unsafe_allow_html=True)
st.markdown('<p class="meu-subtitulo">INTELIGÊNCIA ARTIFICIAL</p>', unsafe_allow_html=True)

# Mensagem de boas vindas estilo notificação
st.toast("Bem Vindo")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("CHAT GPT", "https://streamlit.app")
    
with col2:
    st.link_button("GOOGLE AI", "https://streamlit.app")
    
with col3:
    st.link_button("LOVABLE", "https://remove.bg")
    
# Divisória de Sites Úteis
st.markdown('<div class="sitesuteis-container"><a href="https://google.com" target="_blank" class="sitesuteis">🌐 SITES ÚTEIS</a></div>', unsafe_allow_html=True)
st.markdown('<p class="facilidade">Sites de Facilidade</p>', unsafe_allow_html=True)

col1_inf, col2_inf, col3_inf = st.columns(3)

with col1_inf:
    st.link_button("CHAT GPT", "https://streamlit.app")
    
with col2_inf:
    st.link_button("GOOGLE AI", "https://streamlit.app")
    
with col3_inf:
    st.link_button("remove.bg", "https://remove.bg")
