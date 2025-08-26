import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="🔭 Multi-Messenger Event Correlator", layout="wide")


st.title("🔭 Multi-Messenger Event Correlator")
st.caption("Prototype dashboard for correlating astrophysical events across multiple observatories 🚀")

st.sidebar.header("Filters")
source = st.sidebar.multiselect(
    "Select Event Sources",
    ["GWOSC (Gravitational Waves)", "ZTF (Optical Transients)", "TNS (Transient Name Server)", 
     "NASA HEASARC (High-Energy)", "SIMBAD / Vizier (Catalogs)"],
    default=["GWOSC (Gravitational Waves)", "ZTF (Optical Transients)"]
)
time_window = st.sidebar.slider("Time Correlation Window (± minutes)", 1, 1440, 60)
angle_threshold = st.sidebar.slider("Spatial Correlation Threshold (°)", 0.1, 5.0, 1.0)

data = pd.DataFrame({
    "Source": np.random.choice(source, 12),
    "Event Type": np.random.choice(["Gravitational Wave", "Optical Flash", "Gamma-Ray Burst"], 12),
    "Time (UTC)": pd.date_range("2025-08-20", periods=12, freq="12H"),
    "RA": np.random.uniform(0, 360, 12).round(2),
    "DEC": np.random.uniform(-90, 90, 12).round(2),
    "Confidence Score": np.random.uniform(0.5, 1.0, 12).round(2),
    "Status": np.random.choice(["Isolated", "Possible Correlation", "Strong Correlation"], 12)
})

st.subheader("📊 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Events Fetched", len(data))
col2.metric("Correlated Events", (data["Status"] != "Isolated").sum())
col3.metric("Strong Correlations", (data["Status"] == "Strong Correlation").sum())

st.subheader("📝 Event Data")
st.dataframe(data, use_container_width=True)

st.subheader("📈 Event Insights")
col4, col5 = st.columns(2)

with col4:
    st.bar_chart(data["Event Type"].value_counts())

with col5:
    st.bar_chart(data["Status"].value_counts())

st.subheader("🚨 Alerts")
if (data["Status"] == "Strong Correlation").any():
    st.error("⚡ Potential Multi-Messenger Detection: Correlated events across sources found!")
else:
    st.success("✅ No strong correlations detected at the moment.")

st.markdown("---")
st.caption("⚡ Mock Prototype | Data randomly generated for demo | CTRL+SPACE HACKATHON")
