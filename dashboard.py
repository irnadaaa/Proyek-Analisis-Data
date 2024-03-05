import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Bike Sharing Dashboard")

#DataFrame
day_df = pd.read_csv('day_data.csv')
hour_df = pd.read_csv('hour.csv')


with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/irnadaaa/Proyek-Analisis-Data/assets/raw/main/logo1.png")
    

#Menghitung Jumlah Pengguna Pertahun
total_cnt = day_df.groupby('yr').agg({'cnt': 'sum'}).reset_index()

st.header("User Counts of The Year")

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

#Menghitung Jumlah Pengguna Bulanan di Tahun 2012
monthly_cnt = day_df[day_df['yr'] == 1].groupby('mnth')['cnt'].sum().reset_index()

# Create a Streamlit app
st.header("Number of User per Month (2012)")

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

#Menghitung Jumlah Pengguna Harian di Tahun 2012
# Filter data for the year 2012 and group by weekday
daily_cnt = day_df[day_df['yr'] == 1].groupby('weekday')['cnt'].sum().reset_index()

# Create a Streamlit app
st.header("Number of User per Day (2012)")

# Display the DataFrame with daily counts
st.write("Daily User Counts in 2012:")
st.write(daily_cnt)

# Create a line plot
plt.figure(figsize=(10, 5))
plt.plot(daily_cnt['weekday'], daily_cnt["cnt"], marker='o', linewidth=2, color="green")
plt.title("Number of User per Day (2012)", loc="center", fontsize=20)
plt.xlabel('Weekday')
plt.ylabel('User Count')
plt.xticks(range(0, 7), ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Display the plot in Streamlit
st.pyplot(plt)

#Menghitung Jumlah Pengguna Perjam di Tahun 2012
# Filter data for the year 2012 and group by hour
hourly_cnt = hour_df[hour_df['yr'] == 1].groupby('hr')['cnt'].sum().reset_index()

# Create a Streamlit app
st.header("Number of User per Hour (2012)")

# Display the DataFrame with hourly counts
st.write("Hourly User Counts in 2012:")
st.write(hourly_cnt)

# Create a line plot
plt.figure(figsize=(10, 5))
plt.plot(hourly_cnt['hr'], hourly_cnt["cnt"], marker='o', linewidth=2, color="red")
plt.title("Number of User per Hour (2012)", loc="center", fontsize=20)
plt.xlabel('Hour')
plt.ylabel('User Count')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Display the plot in Streamlit
st.pyplot(plt)

# Group by year and calculate total registered and casual counts
registered_cnt = day_df.groupby('yr')['registered'].sum().reset_index()
casual_cnt = day_df.groupby('yr')['casual'].sum().reset_index()

# Create a Streamlit app
st.header('Comparison of User Type per Year')

# Display the DataFrames with registered and casual counts
st.write("Registered User Counts per Year:")
st.write(registered_cnt)

st.write("Casual User Counts per Year:")
st.write(casual_cnt)

# Create a barplot
plt.figure(figsize=(10, 6))
plt.bar(registered_cnt['yr'], registered_cnt['registered'], color='green', label='Registered')
plt.bar(casual_cnt['yr'], casual_cnt['casual'], color='red', label='Casual')
plt.title('Comparison of User Type per Year')
plt.xlabel('Year')
plt.xticks(range(0, 2), ['2011', '2012'])
plt.ylabel('User Count')
plt.legend(title='User Type', loc='upper right')
plt.tick_params(axis='x', labelsize=12)

# Display the plot in Streamlit
st.pyplot(plt)
