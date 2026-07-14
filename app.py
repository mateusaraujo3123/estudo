import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("teste"):
       st.link_button("HTTPS://www.youTube.com")