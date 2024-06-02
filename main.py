 
# import module
import streamlit as st

st.set_page_config(layout='wide')
 
col1, col2 = st.columns(2)

with col1:
    st.image("/Users/manaskulkarni/VS_Code_Projects/app2_portfolio/images/photo.png")

with col2:
    st.title("Manas Kulkarni")
    content = """
                Hi this is Manas. I'm a python programmer. 
                I work for US Bank
                """
    st.write(content)