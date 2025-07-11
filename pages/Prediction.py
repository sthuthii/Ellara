import streamlit as st
import pickle
import numpy as np
from streamlit_extras.switch_page_button import switch_page
from database import get_average_inputs
from navbar import show_navbar

st.set_page_config(page_title="PCOS Prediction", layout="centered", initial_sidebar_state = "collapsed")
st.title("🔍 PCOS Risk Prediction")

model = pickle.load(open("pcos_model.pkl", "rb"))
show_navbar

if "user_id" in st.session_state:
    if st.button("⚡ Predict from My Average Data"):
        avg_data = get_average_inputs(st.session_state["user_id"])
        if None in avg_data:
            st.warning("Please enter at least one daily log.")
        else:
            avg_array = np.array(avg_data).reshape(1, -1)
            prediction = model.predict(avg_array)[0]
            confidence = model.predict_proba(avg_array)[0][prediction]

            if prediction == 1:
                st.error(f"⚠️ You are **at risk** of PCOS.\n\n🧠 Confidence: {confidence:.2f}")
            else:
                st.success(f"✅ You are **not at risk** of PCOS.\n\n🧠 Confidence: {confidence:.2f}")
else:
    st.warning("Please login first from the homepage.")
