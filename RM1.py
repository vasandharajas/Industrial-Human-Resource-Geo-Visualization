import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
url = 'resource1.csv'  # Replace with your dataset path
df = pd.read_csv(url)

# Clean column names to ensure compatibility with Streamlit and Plotly
df.columns = df.columns.str.replace('[^A-Za-z0-9 ]+', '', regex=True)
df.columns = df.columns.str.replace(' ', '_')  # Replace spaces with underscores for consistency

# Dashboard title
st.title("Workers Population by Industry and Geography")

# Verify column names
st.write("Columns available in the dataset: ", df.columns.tolist())

# Sidebar filters
state = st.sidebar.selectbox('Select State', df['IndiaStates'].unique())

# Filter data based on selections
filtered_df = df[df['IndiaStates'] == state]

# Main Workers Plot
fig_main_workers = px.bar(filtered_df, x='NIC_Name', y='Main_Workers__Total___Persons',
                          title='Main Workers by Industry',
                          labels={'NIC_Name': 'Industry', 'Main_Workers__Total___Persons': 'Workers'})

# Marginal Workers Plot
fig_marginal_workers = px.bar(filtered_df, x='NIC_Name', y='Marginal_Workers__Total___Persons',
                              title='Marginal Workers by Industry',
                              labels={'NIC_Name': 'Industry', 'Marginal_Workers__Total___Persons': 'Workers'})

# Display plots
st.plotly_chart(fig_main_workers)
st.plotly_chart(fig_marginal_workers)

# Correlation matrix
st.header("Correlation Matrix")
numeric_df = df.select_dtypes(include=['float64', 'int64'])  # Exclude non-numeric columns
correlation_matrix = numeric_df.corr()
st.write(correlation_matrix)

# Descriptive statistics
st.header("Descriptive Statistics")
st.write(df.describe())

# Optional: Add additional charts or analysis
# For example, if you want to compare gender-based distribution (if applicable):
if 'Gender' in df.columns:
    fig_gender_distribution = px.pie(df, names='Gender', title='Gender Distribution of Workers')
    st.plotly_chart(fig_gender_distribution)

# Show filtered data for user reference
st.header("Filtered Data")
st.write(filtered_df)