import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="🔭 Multi-Messenger Event Correlator", layout="wide")

st.markdown(
    """
    <style>
    /* Gradient cosmic background */
    .stApp {
        background: radial-gradient(circle at 30% 30%, #1a1a40, #000000 80%);
        color: #c77dff;
    }

    section[data-testid="stSidebar"] {
        background-color: #1b1b2f;
        color: #80ffdb;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #80ffdb !important; /* Cyan glow */
        text-shadow: 0px 0px 12px #80ffdb;
    }

    .stMarkdown, .stCaption, p {
        color: #c77dff !important; /* Purple text */
    }

    div[data-testid="stMetricValue"] {
        color: #ffba08 !important; /* Gold */
        text-shadow: 0px 0px 10px #ffba08;
    }

    .stDataFrame {
        background-color: #111111;
        color: #80ffdb;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
    type_counts = data["Event Type"].value_counts().reset_index()
    type_counts.columns = ["Event Type", "Count"]
    fig1 = px.area(
        type_counts,
        x="Event Type", y="Count",
        title="Event Types Over Observations"
    )
    fig1.update_traces(line_color="#80ffdb", fill="tozeroy", line_shape="spline")
    fig1.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c77dff"),
        title_font=dict(color="#80ffdb")
    )
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    status_counts = data["Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]
    fig2 = px.area(
        status_counts,
        x="Status", y="Count",
        title="Event Status Distribution"
    )
    fig2.update_traces(line_color="#ffba08", fill="tozeroy", line_shape="spline")
    fig2.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c77dff"),
        title_font=dict(color="#80ffdb")
    )
    st.plotly_chart(fig2, use_container_width=True)

# Alerts
st.subheader("🚨 Alerts")
if (data["Status"] == "Strong Correlation").any():
    st.error("⚡ Potential Multi-Messenger Detection: Correlated events across sources found!")
else:
    st.success("✅ No strong correlations detected at the moment.")

st.markdown("---")
st.caption("⚡ Mock Prototype | Data randomly generated for demo | CTRL+SPACE HACKATHON")
