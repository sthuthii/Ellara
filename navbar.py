import streamlit as st

def show_navbar():
    st.markdown(
        """
        <style>
            .navbar {
                background-color: #fce4ec;
                padding: 10px 20px;
                border-radius: 12px;
                display: flex;
                justify-content: space-around;
                font-size: 16px;
                margin-bottom: 20px;
            }
            .navbar a {
                text-decoration: none;
                color: #e91e63;
                font-weight: bold;
            }
            .navbar a:hover {
                color: #ad1457;
            }
        </style>
        <div class="navbar">
            <a href="/">🏠 Home</a>
            <a href="/Daily_Log">📝 Daily Log</a>
            <a href="/Profile">👤 Profile</a>
            <a href="/Logout">🔒 Logout</a>
        </div>
        """,
        unsafe_allow_html=True
    )
