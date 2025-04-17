import streamlit as st
import pickle

with open("traffic_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🚦 AI-TrafficSense")

car_count = st.slider("How many vehicles on the road?", 0, 120, 30)

prediction = model.predict([[car_count]])[0]

status_map = {0: "Clear", 1: "Busy", 2: "Traffic Jam"}
result = status_map[prediction]

if result == "Clear":
    st.success("✅ Road is Clear")
elif result == "Busy":
    st.warning("⚠️ Road is Busy")
else:
    st.error("🚨 Traffic Jam!")

st.write(f"Prediction: **{result}**")
