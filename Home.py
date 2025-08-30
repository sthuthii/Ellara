import streamlit as st

st.set_page_config(page_title="Home", layout="wide", initial_sidebar_state="collapsed")

# Custom Styling for Cards
card_style = """
    <style>
        .card {
            border-radius: 15px;
            padding: 1.2rem;
            margin: 0.5rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            transition: transform 0.2s;
            background-color: #fff0f6;
        }
        .card:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        }
        .title {
            font-size: 20px;
            color: #d81b60;
            font-weight: 600;
            margin-bottom: 0.3rem;
        }
        .desc {
            font-size: 16px;
            color: #6a1b9a;
        }
    </style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# 🌸 Welcome
st.markdown("""
    <h1 style='text-align: center; color: #d81b60;'> Welcome to Your Ellara</h1>
    <p style='text-align: center; font-size: 18px; color:#4a148c;'>Your cozy space to log, track & predict your health 🧘‍♀️💖</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 🔮 Feature Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class='card'>
            <div class='title'>✍️ Daily Log</div>
            <div class='desc'>Log your symptoms, sleep, mood, and cycle status here.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Daily Log"):
        st.switch_page("pages/Daily_Log.py")  # adjust path as needed

    st.markdown("""
        <div class='card'>
            <div class='title'>📚 Education Hub</div>
            <div class='desc'>Learn more about PCOS, symptoms, myths, and healthy habits.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Explore Education Hub"):
        st.switch_page("pages/4_Education_Hub.py")

with col2:
    st.markdown("""
        <div class='card'>
            <div class='title'>🔮 Predict PCOS Risk</div>
            <div class='desc'>Get your risk level based on your health stats.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Start Prediction"):
        st.switch_page("pages/Prediction.py")

    st.markdown("""
        <div class='card'>
            <div class='title'>📊 Visual Insights</div>
            <div class='desc'>Visualize your hormone levels, BMI trends, and other stats.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("View Dashboard"):
        st.switch_page("pages/5_Insights_Dashboard.py")

with col3:
    st.markdown("""
        <div class='card'>
            <div class='title'>📝 Generate Report</div>
            <div class='desc'>Download a beautiful summary PDF of your results and insights.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Generate PDF"):
        st.switch_page("pages/6_Report_Generator.py")

    st.markdown("""
        <div class='card'>
            <div class='title'>💬 Ask PCOS Bot</div>
            <div class='desc'>Chat with an AI assistant to get help or answer PCOS questions.</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Chat with Bot"):
        st.switch_page("pages/7_PCOS_Bot.py")

# 💡 Tip of the Day
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <h4 style='color:#6a1b9a;'>💡 Tip of the Day</h4>
    <p style='color:#4a148c;'>Drink enough water and get 7-8 hours of sleep to improve hormonal balance 💧🌙</p>
""", unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<center><small>Made with 💖 by Sthuthi</small></center>", unsafe_allow_html=True)
