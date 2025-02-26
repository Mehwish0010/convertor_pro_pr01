from PIL import Image
import streamlit as st
import os

# Ensure correct image path
image_path = os.path.join(os.path.dirname(__file__), "assets", "convertor1.jpg")

# Check if image exists before loading
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, width=700)
else:
    st.warning("⚠️ Image not found. Make sure 'convertor1.jpg' is in the 'assets' folder.")

st.title("Convert-Pro Converter App")

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

# Sidebar for selection
option = st.sidebar.selectbox("Select Conversion Type", 
                              ["Temperature", "Length", "Weight"])

if option == "Temperature":
    st.header("🌡 Temperature Converter")
    temp_unit = st.radio("Choose conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
    value = st.number_input("Enter temperature:")
    
    if temp_unit == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(value)
        st.success(f"{value}°C = {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(value)
        st.success(f"{value}°F = {result:.2f}°C")

elif option == "Length":
    st.header("📏 Length Converter")
    length_unit = st.radio("Choose conversion", ["Kilometers to Miles", "Miles to Kilometers"])
    value = st.number_input("Enter length:")
    
    if length_unit == "Kilometers to Miles":
        result = km_to_miles(value)
        st.success(f"{value} km = {result:.2f} miles")
    else:
        result = miles_to_km(value)
        st.success(f"{value} miles = {result:.2f} km")

elif option == "Weight":
    st.header("⚖ Weight Converter")
    weight_unit = st.radio("Choose conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
    value = st.number_input("Enter weight:")
    
    if weight_unit == "Kilograms to Pounds":
        result = kg_to_pounds(value)
        st.success(f"{value} kg = {result:.2f} lbs")
    else:
        result = pounds_to_kg(value)
        st.success(f"{value} lbs = {result:.2f} kg")

st.sidebar.markdown("💡 Created using **Streamlit** 🚀")
