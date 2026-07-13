import streamlit as st

# 1. Configuração da Página (Diz ao navegador o título e o tamanho da tela)
st.set_page_config(
    page_title="Mercadinho",
    layout="centered"  # Faz o site ocupar a tela inteira (da esquerda para a direita)
)

# 2. Criando o Título Principal
st.title("IA`s")
# 3. Criando as Colunas (O esqueleto invisível para colocar objetos lado a lado)
# Aqui criamos as colunas de tamanhos exatamente iguais st.columns(4) é oque diz (tem que ser iguais todas o tamanho)
# basta colocar (col) e o numero e a virgula, e no final colocar = st.columns(quantidade de colunas) para padronizar os tamanhos
col1, col2, col3, col4 = st.columns(4)

# 4. Colocando um botão dentro de cada coluna usando o comando 'with'
with col1:
    if st.button("CHATGPT", use_container_width=True):
        st.write("Você CHAT GPT!")

with col2:
    if st.button("📦 Controlar Estoque", use_container_width=True):
        st.write("Você clicou em Estoque!")

with col3:
    if st.button("📊 Ver Relatórios", use_container_width=True):
        st.write("Você clicou em Relatórios!")

with col4:
    if st.button("📊 Ver Rela", use_container_width=True):
        st.write("Você clicou em Rela!")

# titulo para categorias
st.title("administração")

# repetir colunas com funções diferentes mas com a mesam ideia da anterior
col5, col6, col7, col8 = st.columns(4)

with col5:
    if st.button("🛒 Realizar Ve", use_container_width=True):
        st.write("Você clicou em Ve!")

with col6:
    if st.button("📦 Controlar Es", use_container_width=True):
        st.write("Você clicou em Es!")

with col7:
    if st.button("📊 Ver Re", use_container_width=True):
        st.write("Você clicou em Re!")

with col8:
    if st.button("📊 Ver Rl", use_container_width=True):
        st.write("Você clicou em Rl!")
