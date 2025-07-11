import streamlit as st
from database import register_user, get_user_id

st.set_page_config(page_title="Login", layout="centered")
st.title("🔐 Login / Sign Up")

username = st.text_input("Username")
email = st.text_input("Email")

if st.button("Continue"):
    if username and email:
        register_user(username, email)
        st.session_state["user_id"] = get_user_id(username)
        st.success("Login successful! Redirecting...")

        # Add redirect to Home.py
        st.switch_page("Home.py")
    else:
        st.error("Please enter both username and email.")
