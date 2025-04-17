import streamlit as st
import requests
import pickle
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import time
import os

#Page setup
st.set_page_config(page_title="AI Traffic Jam Dashboard", page_icon="🚦", layout="wide")
st.markdown("<h1 style='text-align: center;'>🚦 AI-TrafficSense</h1>", unsafe_allow_html=True)
st.markdown("---")

# Load trained model
with open("traffic_model.pkl", "rb") as f:
    model = pickle.load(f)

# Auto-refresh every 5 seconds
st_autorefresh(interval=5000, key="refresh")

# Fetch live count from Flask backend
def get_live_vehicle_count():
    try:
        response = requests.get("http://localhost:5000/current_count")
        data = response.json()
        return data.get("count", 0)
    except Exception as e:
        st.error(f"❌ Error fetching count: {e}")
        return 0

# Read historical data
def load_csv_data():
    try:
        return pd.read_csv("vehicle_counts_log.csv", parse_dates=["timestamp"])
    except:
        return pd.DataFrame(columns=["timestamp", "vehicle_count"])

# Get live count
car_count = get_live_vehicle_count()

# Predict traffic condition
prediction = model.predict([[car_count]])[0]
status_map = {0: "Clear", 1: "Busy", 2: "Traffic Jam"}
result = status_map[prediction]

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Live Traffic Simulation")

    if result == "Clear":
        st.success("✅ Road is Clear. Vehicles can move freely.")
    elif result == "Busy":
        st.warning("⚠️ Road is getting busy. Moderate traffic detected.")
    else:
        st.error("🚨 Traffic Jam! Congestion is high.")

    st.markdown("### 📈 Live Vehicle Count Chart")
    df = load_csv_data()
    if not df.empty:
        chart_data = df.tail(30)  # Show last 30 readings
        st.line_chart(chart_data.set_index("timestamp")["vehicle_count"])
    else:
        st.info("No data logged yet.")

with col2:
    st.subheader("📈 Traffic Insights")
    st.metric(label="🚗 Vehicle Count", value=car_count)

    if result == "Clear":
        st.metric(label="⏱️ Avg Wait Time", value="0 - 1 min", delta="-2 min")
        st.metric(label="🌍 Pollution Level", value="Low")
    elif result == "Busy":
        st.metric(label="⏱️ Avg Wait Time", value="3 - 5 min", delta="+1 min")
        st.metric(label="🌍 Pollution Level", value="Moderate")
    else:
        st.metric(label="⏱️ Avg Wait Time", value="8+ min", delta="+5 min")
        st.metric(label="🌍 Pollution Level", value="High")

    st.markdown("---")

    # Download button for the CSV log
    if os.path.exists("vehicle_counts_log.csv"):
        with open("vehicle_counts_log.csv", "rb") as f:
            st.download_button(
                label="📥 Download Vehicle Log CSV",
                data=f,
                file_name="vehicle_counts_log.csv",
                mime="text/csv"
            )

    st.info("Real-time predictions help in adjusting signal timers dynamically.")
