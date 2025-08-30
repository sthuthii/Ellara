import streamlit as st
import plotly.graph_objects as go

# Sample User Data (replace with actual inputs or session_state)
user_data = {
    "name": "Sthuthi",
    "age": 21,
    "cycle_length": 32,
    "period_length": 6,
    "pcos_prediction": "High Risk",
    "risk_score": 78,
    "ovulation_day": 18,
    "fertile_window": "Day 16 - Day 20",
}

# 🚺 Title
st.title("📝 Ellara Health Report Preview")

# 🧍 Basic Info
st.markdown(f"""
**👤 Name:** {user_data['name']}  
**🎂 Age:** {user_data['age']}  
**🩸 Period Length:** {user_data['period_length']} days  
**🔁 Cycle Length:** {user_data['cycle_length']} days  
**🟣 Ovulation Day:** Day {user_data['ovulation_day']}  
**🌼 Fertile Window:** {user_data['fertile_window']}  
""")

# 🔮 PCOS Risk Prediction
st.subheader("🔮 PCOS Risk Prediction")
st.markdown(f"**Prediction:** `{user_data['pcos_prediction']}`")

# 📊 Risk Score Chart
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=user_data['risk_score'],
    title={'text': "PCOS Risk Score"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "#d81b60"},
        'steps': [
            {'range': [0, 30], 'color': '#a5d6a7'},
            {'range': [30, 70], 'color': '#fff59d'},
            {'range': [70, 100], 'color': '#ef9a9a'}
        ]
    }
))
st.plotly_chart(fig, use_container_width=True)

# 📅 Cycle Graph
st.subheader("📅 Cycle & Period Timeline")
cycle_fig = go.Figure()
cycle_fig.add_trace(go.Scatter(
    x=list(range(1, user_data['cycle_length']+1)),
    y=[1 if day <= user_data['period_length'] else 0 for day in range(1, user_data['cycle_length']+1)],
    mode='lines+markers',
    name="Period Days",
    line=dict(color='#d81b60')
))
cycle_fig.add_vline(x=user_data['ovulation_day'], line_dash="dash", line_color="green", annotation_text="Ovulation")
st.plotly_chart(cycle_fig, use_container_width=True)

# 🌿 Health Tips
st.subheader("🌿 Personalized Health Tips")
st.markdown("""
- Include **high-fiber** foods and **anti-inflammatory** meals.
- Maintain a consistent **sleep schedule**.
- Try **low-impact exercises** like yoga, walking, or Pilates.
- Stay hydrated and track your symptoms daily.
""")

# ✅ Proceed to Download
if st.button("✅ Looks Good! Generate PDF"):
    st.switch_page("pages/7_Generate_Report.py")
