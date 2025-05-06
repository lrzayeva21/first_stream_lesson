import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Analytics Dashboard", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Descriptives", "Sales", "Profit"])


descriptives_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 67]
})

sales_data = pd.DataFrame({
    'best_seller_tag__y_or_n': ['Yes', 'No', 'Yes', 'No'],
    'sales_price': [100, 50, 150, 70]
})

profit_data = pd.DataFrame({
    'Region': ['North', 'South', 'East', 'West'],
    'Profit': [200, 300, 150, 400]
})

# Descriptives Page
if page == "Descriptives":
    st.title("Descriptives")
    st.subheader("Descriptive Statistics")
    st.write(descriptives_data.describe())

    fig = px.bar(
        descriptives_data,
        x='Category',
        y='Values',
        title="Category Values",
        color_discrete_sequence=['blue']
    )
    st.plotly_chart(fig)

# Sales Page
elif page == "Sales":
    st.title("Sales Analysis")

    
    fig = px.bar(
        sales_data,
        x='best_seller_tag__y_or_n',
        y='sales_price',
        title="Sales Price by Best Seller Tag",
        labels={'best_seller_tag__y_or_n': 'Best Seller (Y/N)', 'sales_price': 'Sales Price'},
        color_discrete_sequence=['orange']
    )
    st.plotly_chart(fig)

# Profit Page
elif page == "Profit":
    st.title("Profit Analysis")

   
    fig = px.bar(
        profit_data,
        x='Region',
        y='Profit',
        title="Profit by Region",
        labels={'Region': 'Region', 'Profit': 'Profit'},
        color_discrete_sequence=['green']
    )
    st.plotly_chart(fig)
