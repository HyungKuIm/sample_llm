import streamlit as st

name = st.text_input("성함을 입력해 주세요")

if name!="":
    f"안녕하세요 {name}씨"