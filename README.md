# 🇮🇳 India Population Analytics Dashboard

An interactive Streamlit + Plotly dashboard analyzing district-level population demographics in India using government open data (Census).  
This project visualizes population distribution, literacy, gender equality, religion spread, and infrastructure access across 500+ districts.

---

## 🚀 Features

✔ District-level **Geo-visualisation**  
✔ Population + demographics mapping  
✔ Male–Female literacy comparison  
✔ Electricity vs Internet development insights  
✔ Top districts leaderboard  
✔ Fully interactive sidebar filters  
✔ Explore trends state-wise or all-India view  
✔ Responsive and mobile-friendly UI

---

## 🗂 Dataset Fields Used
| Column | Description |
|--------|-------------|
| State name | Indian State |
| District | Name of District |
| Population | Total population |
| Male / Female | Gender split |
| Literate | Total literates |
| Male_Literate / Female_Literate | Literacy by gender |
| Agricultural_Workers | Rural dependency |
| Hindus, Muslims, etc. | Religion breakdown |
| Housholds_with_Electric_Lighting | Basic infrastructure |
| Households_with_Internet | Digital access |
| Latitude / Longitude | Geographic positioning |

Total Rows: **517 districts**

---

## 📊 Visuals Included

| Chart | Insight |
|-------|---------|
| Geo Scatter Map | Population density hotspots |
| Bar Charts | District comparisons |
| Literacy Gap Scatter | Gender inequality |
| Electricity vs Internet | Socio-economic status |
| Top 10 Population | Urban load centers |

---

## 🧠 Key Insights You Can Explore
- Where is gender literacy gap extremely high?
- Which districts lack internet even with good electrification?
- How uneven is religious population distribution?
- Which areas show extreme rural dependency?

This dashboard enables **data-driven governance**, planning, and research.

---

## 🧱 Tech Stack

| Tool | Use |
|------|-----|
| Python | Data Cleaning & Analysis |
| Streamlit | Dashboard UI |
| Plotly Express | Interactive visualizations |
| Pandas | Data wrangling |
| NumPy | Numerical support |

---

## 🔧 Setup Instructions

### 1️⃣ Clone this repo
```bash
git clone https://github.com/<your-username>/india-pop-dashboard.git
cd india-pop-dashboard
