import streamlit as st

# 🎯 App configuration
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

st.title("💪 BMI Calculator")
st.write("Easily calculate your Body Mass Index (BMI) using your height (in cm) and weight (in kg).")

# 🧍 User input
st.subheader("Enter your details:")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (in kilograms)", min_value=0.0, format="%.2f")

with col2:
    height_cm = st.number_input("Height (in centimeters)", min_value=0.0, format="%.2f")

# 🧮 BMI Calculation
if st.button("Calculate BMI"):
    if height_cm > 0 and weight > 0:
        # Convert cm to meters
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        st.success(f"✅ Your BMI is: **{bmi:.2f}**")

        # BMI category
        if bmi < 18.5:
            st.warning("You are **Underweight** 😟")
        elif 18.5 <= bmi < 24.9:
            st.info("You are in the **Normal weight** range 🙂")
        elif 25 <= bmi < 29.9:
            st.warning("You are **Overweight** 😐")
        else:
            st.error("You are **Obese** 😞")
    else:
        st.error("Please enter valid positive values for height and weight.")

# ℹ️ Info
st.write("---")
st.caption("Formula: BMI = weight (kg) / [height (m)]²")
st.caption("Healthy BMI range: 18.5 - 24.9")

