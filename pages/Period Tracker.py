import streamlit as st

# 🌸 Custom theme (defined in config.toml for colors)
st.set_page_config(page_title="Period Tracker", layout="centered")

# Period Tracker Page Header
st.markdown("""
    <h1 style='text-align: center; color: #d81b60;'>Track Your Periods 🩸</h1>
    <p style='text-align: center; font-size: 18px;'>Keep track of your menstrual cycle for better health management.</p>
""", unsafe_allow_html=True)

# Input Form to Track Periods
with st.form("period_form"):
    period_start = st.date_input("Start Date of Period")
    period_end = st.date_input("End Date of Period")
    cycle_length = st.number_input("Average Cycle Length (days)", min_value=20, max_value=60, value=28)
    symptoms = st.text_area("Symptoms experienced during this period")

    submit_button = st.form_submit_button("Save Period Entry")

    if submit_button:
        # In reality, you'd save the data in a database or a file
        st.success(f"Your period from {period_start} to {period_end} has been saved!")
        # Example of saving data (you can expand this):
        # add_period_entry(period_start, period_end, cycle_length, symptoms)
