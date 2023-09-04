import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="CSV Dashboard Builder",
    page_icon=":bar_chart:",
    layout="wide",
)

# Define a function to load and analyze the dataset
def load_and_analyze_data(uploaded_file):
    if uploaded_file is not None:
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(uploaded_file)

        # Header and description with updated colors
        st.title("📊 CSV Dashboard Builder")
        st.sidebar.title("Settings")
        st.markdown(
            """
            Analyze and visualize your CSV data with this beautiful dashboard. Upload your dataset using the file uploader on the left sidebar.
            """
        )

        # Show the DataFrame
        st.subheader("Dataset Preview")
        st.write(df)

        # Basic dataset statistics
        st.subheader("Dataset Statistics")
        st.write(df.describe())

        # Data Visualization
        st.subheader("Data Visualization")

        # Select columns for plotting
        columns = st.multiselect("Select columns for plotting", df.columns)

        if columns:
            # Create a scatter plot for selected columns
            scatter_fig = px.scatter(
                df, x=columns[0], y=columns[1], title="Scatter Plot"
            )
            st.plotly_chart(scatter_fig)

            # Create a bar chart for selected columns
            bar_fig = px.bar(df, x=columns[0], y=columns[1], title="Bar Chart")
            st.plotly_chart(bar_fig)

# Sidebar background color with updated color
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #003049; /* Dark blue */
        color: #FFFFFF; /* White text */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main content background color with updated color
st.markdown(
    """
    <style>
    .main {
        background-color: #F0F3BD; /* Light yellow */
    }
    .main * {
        color: #003049; /* Dark blue text */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Call the function to load and analyze the data
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
load_and_analyze_data(uploaded_file)
