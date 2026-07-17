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

# 1. Função para carregar o CSS local
def load_css(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 2. Executa a função passando o seu arquivo
load_css("style.css")

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
