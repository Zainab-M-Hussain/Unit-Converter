import streamlit as st
from forex_python.converter import CurrencyRates
from pint import UnitRegistry

# Initialize Unit Registry
ureg = UnitRegistry()

# Streamlit app configuration
st.set_page_config(page_title="Google-Style Unit Converter", page_icon="🔄")
st.title("🔄 Google-Style Unit Converter")

# Conversion categories
categories = ["Length", "Weight", "Temperature", "Currency"]
selected_category = st.selectbox("Select Conversion Type", categories)

if selected_category == "Length":
    length_units = ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"]
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)
    value = st.number_input("Enter Value", min_value=0.0, step=0.1)
    
    if st.button("Convert"):
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif selected_category == "Weight":
    weight_units = ["kilogram", "gram", "pound", "ounce"]
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)
    value = st.number_input("Enter Value", min_value=0.0, step=0.1)
    
    if st.button("Convert"):
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif selected_category == "Temperature":
    temp_units = ["celsius", "fahrenheit", "kelvin"]
    from_unit = st.selectbox("From", temp_units)
    to_unit = st.selectbox("To", temp_units)
    value = st.number_input("Enter Value", step=0.1)
    
    if st.button("Convert"):
        if from_unit == to_unit:
            result = value
        elif from_unit == "celsius" and to_unit == "fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "celsius" and to_unit == "kelvin":
            result = value + 273.15
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            result = (value - 32) * 5/9
        elif from_unit == "fahrenheit" and to_unit == "kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "kelvin" and to_unit == "celsius":
            result = value - 273.15
        elif from_unit == "kelvin" and to_unit == "fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif selected_category == "Currency":
    c = CurrencyRates()
    from_currency = st.text_input("From Currency (e.g., USD, EUR, PKR)", value="USD").upper()
    to_currency = st.text_input("To Currency (e.g., USD, EUR, PKR)", value="PKR").upper()
    value = st.number_input("Enter Amount", min_value=0.0, step=0.1)
    
    if st.button("Convert"):
        try:
            result = c.convert(from_currency, to_currency, value)
            st.success(f"{value} {from_currency} = {result:.2f} {to_currency}")
        except:
            st.error("Invalid currency code or network error.")
