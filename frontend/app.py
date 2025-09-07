import streamlit as st
import requests

st.set_page_config(page_title="Exam Prep Agent", page_icon="📘")
st.title("📘 Exam Prep Agent — Phase 1")

st.write("Click the button to test backend connectivity.")

if st.button("Ping Backend"):
    try:
        resp = requests.get("http://127.0.0.1:8000/")
        data = resp.json()
        st.success(f"✅ {data.get('message', 'OK')}")
    except Exception as e:
        st.error(f"❌ Could not connect to backend.\n\n{e}")
