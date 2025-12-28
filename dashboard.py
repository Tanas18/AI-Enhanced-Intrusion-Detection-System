import streamlit as st
import random
import time

st.set_page_config(page_title="AI IDS", layout="centered")

st.title("🛡️ AI-Enhanced Intrusion Detection System")

status_placeholder = st.empty()

while True:
    status = random.choice(["Normal", "Attack"])

    if status == "Normal":
        status_placeholder.success("✅ Network Status: SAFE")
    else:
        status_placeholder.error("🚨 Network Status: ATTACK DETECTED")

    time.sleep(2)
