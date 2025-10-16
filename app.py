import streamlit as st

# 🎯 App title
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

st.title("💪 BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) easily!")

# 🧍 Input fields
st.subheader("Enter your details:")

# Use two columns for better layout
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (in kilograms)", min_value=0.0, format="%.2f")

with col2:
    height = st.number_input("Height (in meters)", min_value=0.0, format="%.2f")

# 🧮 Calculate BMI
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)

        st.success(f"✅ Your BMI is: **{bmi:.2f}**")

        # Health category based on BMI
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

# ℹ️ Extra info
st.write("---")
st.caption("BMI = weight (kg) / [height (m)]²")
st.caption("Healthy BMI range: 18.5 - 24.9")

