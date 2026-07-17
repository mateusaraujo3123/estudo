import streamlit as st
import pandas as pd

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="MERCADINHO Portal Da Vila",
    page_icon="🛍️",
    layout="wide"
)

import streamlit as st

def carregar_css():
    with open("style.css", "r", encoding="utf-8") as arquivo_css:
        st.markdown(f"<style>{arquivo_css.read()}</style>", unsafe_allow_html=True)

# Chame logo após st.set_page_config()
st.set_page_config(
    page_title="Meu App",
    page_icon="🎨",
    layout="wide"
)

carregar_css()
# Cabeçalho Principal (Idêntico ao seu print original)
st.markdown("""
    <div class="main-header">
        <span>🛍️ MERCADINHO Portal Da Vila</span>
        <span class="status-bd">🟢 online</span>
    </div>
""", unsafe_allow_html=True)

# Bloco de Botões Roxos com o Alinhamento e Tamanho Perfeitos
st.markdown("""
    <div class="button-container">
        <a href="/Fiados" target="_self" class="purple-button">👥 FIADOS</a>
        <a href="/Precos" target="_self" class="purple-button">📦 PREÇOS</a>
        <a href="#" target="_self" class="purple-button">📋 CONTAS A RECEBER</a>
    </div>
""", unsafe_allow_html=True)
    
st.markdown("<br>", unsafe_allow_html=True)

# Seção Central Automatizada (2 colunas)
col_centro1, col_centro2 = st.columns(2)
