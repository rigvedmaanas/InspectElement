import streamlit as st
import requests

code = "Enter a Url To tryout"
def Inspect():
    try:
        with st.spinner("Please Wait...."):
            r = requests.get(URL)
        code = r.content.decode()
        c.code(code, language="html")
    except Exception as e:
        c.error(e)


st.write("# Inspect Element")
st.write("**Have you ever needed Inspect Element in your mobile phone/tab? This application will help you see the source code of any website :)**")
c = st.container()
URL = c.text_input("**URL**", placeholder="https://www.example.com")
c.button("Inspect Element", on_click=Inspect)
