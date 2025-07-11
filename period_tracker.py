import streamlit as st
import datetime
import sqlite3




DB_NAME = "pcos_tracker.db"

def init_period_tracker_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS period_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            period_start DATE,
            cycle_length INTEGER,
            period_duration INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()

def save_period_entry(user_id, start_date, cycle_length, duration):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO period_entries (user_id, period_start, cycle_length, period_duration)
        VALUES (?, ?, ?, ?)
    ''', (user_id, start_date, cycle_length, duration))
    conn.commit()
    conn.close()

def get_period_entries(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT period_start, cycle_length, period_duration
        FROM period_entries
        WHERE user_id = ?
        ORDER BY period_start
    ''', (user_id,))
    entries = c.fetchall()
    conn.close()
    return entries

def predict_next_period(user_id):
    entries = get_period_entries(user_id)
    if not entries:
        return None
    last_start, cycle_len, _ = entries[-1]
    last_start = datetime.datetime.strptime(last_start, "%Y-%m-%d").date()
    return last_start + datetime.timedelta(days=cycle_len)

def period_tracker(user_id):
    st.header("📅 Period Tracker")

    st.subheader("➕ Add New Period Entry")
    period_start = st.date_input("Period Start Date", datetime.date.today())
    cycle_length = st.number_input("Average Cycle Length (days)", min_value=20, max_value=45, value=28)
    period_duration = st.number_input("Period Duration (days)", min_value=1, max_value=10, value=5)

    if st.button("Save Entry"):
        save_period_entry(user_id, period_start, cycle_length, period_duration)
        st.success("Entry saved successfully!")

    st.markdown("---")
    entries = get_period_entries(user_id)
    if entries:
        st.subheader("🗓️ Past Period Entries")
        for entry in reversed(entries):
            st.markdown(f"• Start: **{entry[0]}** | Cycle: {entry[1]} days | Duration: {entry[2]} days")

        next_period = predict_next_period(user_id)
        if next_period:
            st.info(f"📍 Your predicted next period is: **{next_period.strftime('%B %d, %Y')}**")
    else:
        st.info("No entries yet.")
import os
st.text(f"DB Path: {os.path.abspath(DB_NAME)}")
