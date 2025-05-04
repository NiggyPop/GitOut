
import streamlit as st
import pandas as pd
import plotly.express as px

# Data
data = {
    "Year": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Deportations (ICE)": [226119, 256085, 267258, 185884, 59011, 72177, 143000, 271484],
    "Asylum Seekers": [287135, 313242, 341715, 340846, 339179, 363059, 409202, None],
    "DACA Recipients": [689800, 699350, 652880, 641000, 611470, 589660, 580000, 580000],
    "TPS Holders": [325000, 318000, 317000, 319000, 320000, 345000, 350000, 350000],
    "Immigrant Visas": [559536, 533557, 462422, 240526, 285069, 493448, 562976, None],
    "Nonimmigrant Visas": [10381491, 9028026, 8742068, 4013210, 2792083, 6815120, 10438327, None]
}
df = pd.DataFrame(data)

# Streamlit UI
st.title("U.S. Immigration Metrics (FY 2017–2024)")
metric = st.selectbox("Select a metric to visualize:", df.columns[1:])

fig = px.bar(df, x="Year", y=metric, title=f"{metric} by Fiscal Year", text=metric)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(yaxis_title="Count", xaxis_title="Fiscal Year", height=600)

st.plotly_chart(fig)
