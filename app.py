import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st

st.set_page_config(page_title="India Population Dashboard", layout="wide")
st.title("🗺️ India Population Distribution — District Level")

@st.cache_data
def load_data():
    return pd.read_csv('pop_india.csv')

df = load_data()

st.sidebar.header("Filters")

states = df["State name"].unique().tolist()
states.insert(0,'Overall India')

state_choice = st.sidebar.selectbox('Select a State:', states)

# Fixed Logic


metric_options = [
    "Population",
    "Male",
    "Female",
    "Literate",
    "Male_Literate",
    "Female_Literate",
    "Agricultural_Workers",
    "Hindus",
    "Muslims",
    "Christians",
    "Sikhs",
    "Buddhists",
    "Jains",
    "Others_Religions",
    "Housholds_with_Electric_Lighting",
    "Households_with_Internet"
]

metric_1 = st.sidebar.selectbox("Main Metric:", metric_options, index=0)
metric_2 = st.sidebar.selectbox("Comparison Metric:", metric_options, index=3)
if state_choice == 'Overall India':
    filtered_df = df
    fig = px.scatter_map(
    filtered_df,
    lat="Latitude",
    lon="Longitude",
    size=metric_1,
    color=metric_1,
    hover_name="District",
    zoom=3,
    height=700,
    color_continuous_scale=px.colors.cyclical.IceFire ,
    title=f"{metric_1} Distribution — {state_choice}",
)
else:
    filtered_df = df[df['State name'] == state_choice]
    fig = px.scatter_map(
    filtered_df,
    lat="Latitude",
    lon="Longitude",
    size=metric_1,
    color=metric_1,
    hover_name="District",
    zoom=6,
    height=700,
    color_continuous_scale=px.colors.cyclical.IceFire ,
    title=f"{metric_1} Distribution — {state_choice}",
)
fig.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig, use_container_width=True)

st.subheader(f"{metric_2} Color — {state_choice}")
fig2 = px.bar(
    filtered_df.sort_values(metric_2, ascending=False),
    x="District",
    y=metric_2,
    text_auto='.2s',
    color=filtered_df[metric_2]
)
st.plotly_chart(fig2, use_container_width=True) 
# Literacy Gap Analysis
st.subheader("📚 Male vs Female Literacy Gap")
fig3 = px.scatter(
    filtered_df,
    x="Male_Literate",
    y="Female_Literate",
    color="State name",
    size="Population",
    hover_name="District",
    trendline="ols"
)
st.plotly_chart(fig3, use_container_width=True)


# Electricity vs Internet Access
st.subheader("⚡ Electricity vs Internet Access")
filtered_df["Internet_Ratio"] = filtered_df["Households_with_Internet"] / filtered_df["Population"]
filtered_df["Electricity_Ratio"] = filtered_df["Housholds_with_Electric_Lighting"] / filtered_df["Population"]

fig4 = px.scatter(
    filtered_df,
    x="Electricity_Ratio",
    y="Internet_Ratio",
    size="Population",
    hover_name="District",
    color="State name",
)
st.plotly_chart(fig4, use_container_width=True)


# Top 10 Most Populated Districts
st.subheader("🏆 Top 10 Most Populated Districts")
top10 = filtered_df.nlargest(10, "Population")

fig5 = px.bar(
    top10,
    x="District",
    y="Population",
    color="Population",
    text_auto='.2s'
)
st.plotly_chart(fig5, use_container_width=True)

