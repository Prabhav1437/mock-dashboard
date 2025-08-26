
# 🌌 Multi-Messenger Event Correlator

A **Streamlit-based mock dashboard** designed to simulate a system that fetches **astrophysical event data** from multiple sources and identifies potentially related events based on **spatial and temporal proximity**.

This prototype illustrates how astrophysical observatories (e.g., GWOSC, ZTF, TNS, NASA HEASARC, SIMBAD) could be combined to detect significant cosmic events (e.g., **neutron star mergers, gamma-ray bursts, black hole collisions**) by correlating signals from **light, gravitational waves, and high-energy particles**.

---

## 📌 Features

* 📡 **Mock Event Fetching** from multiple astrophysics catalogs
* ⏳ **Time Correlation** – checks if events happened within a defined time window
* 🌍 **Spatial Correlation** – compares celestial coordinates (RA/Dec) with angular thresholds
* 🔭 **Cross-Messenger Correlation** – aligns gravitational, optical, and high-energy events
* 📊 **Dashboard UI** with event tables, correlation scores, and mock plots

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit** – dashboard & UI
* **Pandas** – event data handling
* **Plotly / Matplotlib** – for visualizations
* *(Future: AstroPy, APIs from GWOSC, ZTF, TNS, NASA HEASARC)*

---

## 📂 Project Structure

```
📁 multi-messenger-dashboard
 ├── app.py              # Main Streamlit app
 ├── requirements.txt    # Python dependencies
 ├── README.md           # Documentation
 └── mock_data/          # (Optional) synthetic event datasets
```

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/multi-messenger-dashboard.git
cd multi-messenger-dashboard
```

### 2️⃣ (Optional) Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Dashboard

```bash
streamlit run app.py
```

---

## 📊 Example Dashboard View

* Event Tables (mock events with source, time, RA/Dec, type)
* Correlation Check (time + spatial overlap)
* Visualization of correlated events
* Confidence Score (mock percentage for overlap)

---

## 🚀 Future Enhancements

* Real **API integration** with GWOSC, ZTF, TNS, NASA HEASARC
* Use of **AstroPy** for celestial coordinate transformations
* Machine Learning for **event classification & correlation scoring**
* Real-time **multi-messenger alerts**

---

## 🤝 Contribution

1. Fork this repo
2. Create a new branch (`feature-new`)
3. Commit your changes
4. Open a Pull Request 🚀

---
