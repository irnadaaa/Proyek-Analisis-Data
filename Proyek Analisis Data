import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
day_df = pd.read_csv('day.csv')

total_cnt = day_df.groupby('yr').agg({'cnt': 'sum'}).reset_index()

st.title("User Counts of The Year")

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
