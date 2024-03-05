import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Bike Sharing Dashboard")

day_df = pd.read_csv('day.csv')

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


monthly_cnt = day_df[day_df['yr'] == 1].groupby('mnth')['cnt'].sum().reset_index()

# Create a Streamlit app
st.heading("Number of User per Month (2012)")

# Display the DataFrame with monthly counts
st.write("Monthly User Counts in 2012:")
st.write(monthly_cnt)

# Create a line plot
plt.figure(figsize=(10, 5))
plt.plot(monthly_cnt['mnth'], monthly_cnt["cnt"], marker='o', color='purple', linewidth=2)
plt.title("Number of User per Month (2012)", loc="center", fontsize=20)
plt.xlabel('Month')
plt.ylabel('User Count')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Display the plot in Streamlit
st.pyplot(plt)
