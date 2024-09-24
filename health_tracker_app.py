import streamlit as st
import pandas as pd
import numpy as np

def calculate_bmi(weight, height_in_meters):

    if height_in_meters <= 0:
        return None, "Height must be greater than 0."
    
    # Calculate BMI
    bmi = weight / (height_in_meters ** 2)
    bmi = round(bmi, 2)

    # Classify BMI
    if bmi < 18.5:
        category = "Underweight"
        color = "red"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal"
        color = "green"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"
    
    return bmi, category, color

def convert_height_to_meters(feet, inches):

    total_inches = (feet * 12) + inches
    height_in_meters = total_inches * 0.0254
    return height_in_meters

# Streamlit app
st.markdown("<h1 style='text-align: center; color: purple;'>Your BMI Tracker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Based on the inputs you provided</p>", unsafe_allow_html=True)

st.header("Your basic details")

# User input for height, weight, age, and gender
st.write("##### Height:")
col1, col2 = st.columns(2)
with col1:
    feet = st.number_input("Feet:", min_value=0, step=1)
with col2:
    inches = st.number_input("Inches:", min_value=0, max_value=11, step=1)

weight = st.number_input("##### Weight (in kg):", min_value=1.0)
age = st.number_input("##### Age (in years):", min_value=1, step=1)
gender = st.radio("##### Gender:", ('Male', 'Female', 'Other'))

# Convert height to meters
height_in_meters = convert_height_to_meters(feet, inches)

# Calculate BMI
if st.button("Calculate BMI"):
    bmi, category, color = calculate_bmi(weight, height_in_meters)
    
    # Display the BMI and category in a nice format
    st.subheader(f"BMI: {bmi}")
    st.markdown(f"<h3 style='color: {color};'>{category}</h3>", unsafe_allow_html=True)

    # Display additional information with icons, using markdown for a styled message
    st.markdown(f"<div style='background-color: #f0f8ff; padding: 10px; border-radius: 5px;'>"
                f"<p>Your BMI is in the <b>{category}</b> range.</p>"
                f"<p>Normal BMI falls between 18.5 to 24.9.</p>"
                f"<p style='color: grey;'>See how this is calculated.</p>"
                f"</div>", unsafe_allow_html=True)
