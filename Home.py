import streamlit as st

# 🌸 Custom theme (defined in config.toml for colors)
st.set_page_config(page_title="Home", layout="centered", initial_sidebar_state="collapsed")

# 🌼 Welcome Message
st.markdown("""
    <h1 style='text-align: center; color: #d81b60;'>Welcome to Your PCOS Tracker 🌸</h1>
    <p style='text-align: center; font-size: 18px;'>Your cozy space to log, track & predict your health 🧘‍♀️💖</p>
""", unsafe_allow_html=True)

# 🧁 Add Two Column Layout for Cute Cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### ✍️ Start Logging")
    st.info("Head over to the **Daily Log** page and input your health stats for today!")

with col2:
    st.markdown("#### 🔮 Predict PCOS Risk")
    st.success("Check your PCOS risk using your average health data.")

# 💡 Tip
st.markdown("""
<hr>
<h4 style='color:#6a1b9a;'>💡 Tip of the Day</h4>
<p style='color:#4a148c;'>Drink enough water and get 7-8 hours of sleep to improve hormonal balance 💧🌙</p>
""", unsafe_allow_html=True)
