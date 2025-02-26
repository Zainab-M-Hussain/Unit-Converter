import streamlit as st

# Define conversion functions and formulas
def convert_length(value, from_unit, to_unit):
    conversions = {
        'meter': 1,
        'kilometer': 0.001,
        'centimeter': 100,
        'millimeter': 1000,
        'inch': 39.3701,
        'foot': 3.28084,
        'yard': 1.09361,
        'mile': 0.000621371
    }
    formula = f"{value} {from_unit} * {conversions[to_unit]} / {conversions[from_unit]}"
    return value * conversions[to_unit] / conversions[from_unit], formula

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'kilogram': 1,
        'gram': 1000,
        'milligram': 1e6,
        'pound': 2.20462,
        'ounce': 35.274
    }
    formula = f"{value} {from_unit} * {conversions[to_unit]} / {conversions[from_unit]}"
    return value * conversions[to_unit] / conversions[from_unit], formula

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        formula = f"({value} * 9/5) + 32"
        return (value * 9/5) + 32, formula
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        formula = f"({value} - 32) * 5/9"
        return (value - 32) * 5/9, formula
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        formula = f"{value} + 273.15"
        return value + 273.15, formula
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        formula = f"{value} - 273.15"
        return value - 273.15, formula
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        formula = f"({value} - 32) * 5/9 + 273.15"
        return (value - 32) * 5/9 + 273.15, formula
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        formula = f"({value} - 273.15) * 9/5 + 32"
        return (value - 273.15) * 9/5 + 32, formula
    else:
        return value, "No conversion needed"

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="wide")

st.title(" Unit Converter")
st.write("Convert between different units easily!")

# Sidebar for unit selection
unit_type = st.sidebar.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

if unit_type == "Length":
    units = ['meter', 'kilometer', 'centimeter', 'millimeter', 'inch', 'foot', 'yard', 'mile']
elif unit_type == "Weight":
    units = ['kilogram', 'gram', 'milligram', 'pound', 'ounce']
elif unit_type == "Temperature":
    units = ['celsius', 'fahrenheit', 'kelvin']

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From", units)
    value = st.number_input("Value", value=1.0)

with col2:
    to_unit = st.selectbox("To", units)

if st.button("Convert"):
    if unit_type == "Length":
        result, formula = convert_length(value, from_unit, to_unit)
    elif unit_type == "Weight":
        result, formula = convert_weight(value, from_unit, to_unit)
    elif unit_type == "Temperature":
        result, formula = convert_temperature(value, from_unit, to_unit)

    st.success(f"Converted Value: {result:.2f} {to_unit}")
    st.info(f"Conversion Formula: {formula}")

# Footer
st.markdown("---")