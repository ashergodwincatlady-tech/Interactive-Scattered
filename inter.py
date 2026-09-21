import streamlit as st
import plotly.express as px

st.title("My Interactive Chart Maker")

x_values = st.text_input("Enter X values separated by commas:")
y_values = st.text_input("Enter Y values separated by commas:")

if x_values and y_values:
    x = [float(value) for value in x_values.split(",")]
    y = [float(value) for value in y_values.split(",")]

    fig = px.scatter(
        x=x,
        y=y,
        title="My Scatter Plot"
    )

    st.plotly_chart(fig)