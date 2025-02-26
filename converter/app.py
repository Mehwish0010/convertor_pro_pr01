from PIL import Image
import streamlit as st

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

# Streamlit UI
image = Image.open("assets/convertor1.jpg")

st.image(image, width = 700)
st.title("Convert-Pro Convertor App")

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
    st.header("Length Converter")
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
