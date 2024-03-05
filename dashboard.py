import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Bike Sharing Dashboard")

day_df = pd.read_csv('day.csv')
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/irnadaaa/Proyek-Analisis-Data/blob/main/logo.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
sns.set(style='dark')


total_cnt = day_df.groupby('yr').agg({'cnt': 'sum'}).reset_index()

st.heading("User Counts of The Year")

st.write("Total User Counts per Year:")
st.write(total_cnt)

plt.figure(figsize=(10, 5))
sns.barplot(x='yr', y='cnt', hue='yr', legend=False, data=total_cnt, palette='dark')
plt.title("User Counts of The Year", loc="center", fontsize=15)
plt.ylabel("User Count")
plt.xlabel("Year")
plt.xticks(range(0, 2), ['2011', '2012'])
plt.tick_params(axis='x', labelsize=12)

st.pyplot(plt)


