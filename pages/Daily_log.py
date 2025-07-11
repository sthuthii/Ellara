import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from database import add_daily_log, get_user_logs, get_average_inputs

# Load the trained PCOS model
model = pickle.load(open("pcos_model.pkl", "rb"))

# Set page configuration
st.set_page_config(page_title="Daily Health Entry", layout="wide")
st.title("📝 Daily Health Entry")

# Custom styling for better UI
st.markdown("""
    <style>
        .big-font { font-size: 30px; }
        .small-font { font-size: 18px; }
        .card { 
            background-color: #f0f8ff; 
            padding: 20px; 
            border-radius: 10px; 
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .metric-header { color: #0066cc; font-weight: bold; font-size: 22px; }
    </style>
""", unsafe_allow_html=True)

# Check if user is logged in
if "user_id" not in st.session_state:
    st.warning("Please log in first to access this page.")
    st.stop()

# -------- DAILY HEALTH ENTRY -------- #
st.markdown("---")
st.header("🩺 Enter Today's Health Data")
st.markdown("<p class='small-font'>Please fill in the data for today's health entry.</p>", unsafe_allow_html=True)

# Inputs organized in columns for better layout
col1, col2 = st.columns(2)
with col1:
    Age = st.number_input("Age (years)", 10, 60)
    Weight = st.number_input("Weight (kg)", 30.0, 150.0)
    Height = st.number_input("Height (cm)", 120.0, 200.0)
    Cycle_R_I = st.number_input("Cycle (Regular=1 / Irregular=0)", 0, 1)
    Cycle_length_days = st.number_input("Cycle Length (days)", 0, 60)

with col2:
    Marriage_Status_Yrs = st.number_input("Years since marriage", 0, 40)
    Pregnant_Y_N = 1 if st.radio("Ever been pregnant?", ["No", "Yes"]) == "Yes" else 0
    Hip = st.number_input("Hip (inches)", 20.0, 60.0)
    Waist = st.number_input("Waist (inches)", 20.0, 60.0)
    Waist_Hip = Waist / Hip if Hip != 0 else 0

# Function to handle yes/no radio button inputs
def yn_radio(label):
    return 1 if st.radio(label, ["No", "Yes"]) == "Yes" else 0

# Additional health parameters
Weight_gain = yn_radio("Weight gain?")
Hair_growth = yn_radio("Hair growth?")
Skin_darkening = yn_radio("Skin darkening?")
Hair_loss = yn_radio("Hair loss?")
Pimples = yn_radio("Pimples?")
Fast_food = yn_radio("Frequent fast food?")
Reg_exercise = yn_radio("Regular exercise?")
Irregular_periods = yn_radio("Irregular Periods?")

# Submit Entry button
if st.button("📥 Submit Today’s Entry"):
    data = [
        Age, Weight, Height, Weight / ((Height / 100) ** 2), Cycle_R_I, Cycle_length_days,
        Marriage_Status_Yrs, Pregnant_Y_N, Hip, Waist, Waist_Hip,
        Weight_gain, Hair_growth, Skin_darkening, Hair_loss,
        Pimples, Fast_food, Reg_exercise, Irregular_periods
    ]
    add_daily_log(st.session_state["user_id"], data)
    st.success("✅ Today's data saved!")

# Reminder if not logged today
logs = get_user_logs(st.session_state["user_id"])
today = datetime.date.today()
logged_today = any(datetime.datetime.strptime(row[0], "%Y-%m-%d").date() == today for row in logs)

if not logged_today:
    st.warning("🔔 You haven't submitted today's log yet. Keep tracking!")

# -------- PREDICTION -------- #
st.markdown("---")
st.header("🔍 PCOS Risk Prediction")
st.markdown("<p class='small-font'>Click the button to get a prediction of your PCOS risk based on your average data.</p>", unsafe_allow_html=True)

if st.button("⚡ Predict from My Average Data"):
    avg_data = get_average_inputs(st.session_state["user_id"])
    if None in avg_data:
        st.warning("Please submit at least one daily log to generate prediction.")
    else:
        avg_array = np.array(avg_data).reshape(1, -1)
        prediction = model.predict(avg_array)[0]
        confidence = model.predict_proba(avg_array)[0][prediction]

        if prediction == 1:
            st.error(f"⚠️ You are **at risk** of PCOS.\n\n🧠 Confidence: {confidence:.2f}")
        else:
            st.success(f"✅ You are **not at risk** of PCOS.\n\n🧠 Confidence: {confidence:.2f}")

# -------- GRAPH -------- #
st.markdown("---")
st.header("📊 Your Progress Over Time")
st.markdown("<p class='small-font'>View your health progress over time in the graph below.</p>", unsafe_allow_html=True)

if logs:
    df = pd.DataFrame(logs, columns=[ 
        "Date", "Age", "Weight", "Height", "BMI", "Cycle_R_I", "Cycle_length_days",
        "Marriage_Status_Yrs", "Pregnant_Y_N", "Hip", "Waist", "Waist_Hip_Ratio",
        "Weight_gain_Y_N", "Hair_growth_Y_N", "Skin_darkening_Y_N", "Hair_loss_Y_N",
        "Pimples_Y_N", "Fast_food_Y_N", "Reg_Exercise_Y_N", "Irregular_Periods"
    ])
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    # Metric selection with a visually enhanced header
    st.markdown("<p class='metric-header'>📈 Choose a metric to view:</p>", unsafe_allow_html=True)
    metric = st.selectbox("", ["Weight", "BMI", "Cycle_length_days", "Waist_Hip_Ratio"])

    # Plotting the graph with enhanced aesthetics
    fig, ax = plt.subplots(figsize=(10, 5))
    df[metric].plot(ax=ax, marker="o", linestyle="-", color="teal")
    ax.set_title(f"{metric} Over Time", fontsize=16)
    ax.set_ylabel(metric, fontsize=14)
    ax.set_xlabel("Date", fontsize=14)
    st.pyplot(fig)
else:
    st.info("Enter some logs to visualize your health trends.")
