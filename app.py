import streamlit as st

# 1. Configuração da Página (Diz ao navegador o título e o tamanho da tela)
st.set_page_config(
    page_title="Mercadinho Portal Da Vila",
    layout="wide"  # Faz o site ocupar a tela inteira (da esquerda para a direita)
)

# 2. Criando o Título Principal
st.title("🛍️ MERCADINHO Portal Da Vila")
# 3. Criando as Colunas (O esqueleto invisível para colocar objetos lado a lado)
# Aqui criamos 3 colunas de tamanhos exatamente iguais
col1, col2, col3, col4 = st.columns(4)

# 4. Colocando um botão dentro de cada coluna usando o comando 'with'
with col1:
    if st.button("🛒 Realizar Venda", use_container_width=True):
        st.write("Você clicou em Vendas!")

with col2:
    if st.button("📦 Controlar Estoque", use_container_width=True):
        st.write("Você clicou em Estoque!")

with col3:
    if st.button("📊 Ver Relatórios", use_container_width=True):
        st.write("Você clicou em Relatórios!")

with col4:
    if st.button("📊 Ver Rela", use_container_width=True):
        st.write("Você clicou em Rela!")
