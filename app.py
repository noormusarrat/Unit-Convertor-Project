import streamlit as st

# Force light theme for Streamlit
st.set_page_config(page_title="Unit Converter", layout="wide", initial_sidebar_state="expanded")

# Apply custom CSS
st.markdown(
    """
    <style>
        body, .main, .stApp {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        h1, h2, h3, h4, h5, h6, span, p, label {
            color: #2c2c54 !important;
            text-align: center;
        }

        div{
            color: #b3b3de !important;
            text-align: center;
        }

        .stButton>button {
            background: linear-gradient(45deg, #81b3e1, #b8a6eb);
            color: white;
            font-size: 25px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
            box-shadow: 0px 5px 15px rgba(0, 201, 225, 0.4);
            text-align: center;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background: linear-gradient(45deg, #92fe9d, #00c9ff);
            color: black;
        }

        .result-box {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(45deg, #d0e1d2, #00c9ff);
            padding: 25px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 5px 15px rgba(0, 201, 225, 0.3);
            color: #9292e3 !important;
        }
        /* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #cdcde6 !important;  
    color: #f5f1f1 !important; 
    color: #f5f1f1 !important; 
    box-color: #f5f1f1 !important;          
}

    [data-testid="stSidebar"] {
        background-color: #d5d2ea;
    }

    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] select,
    [data-testid="stSidebar"] div[role="combobox"] {
        color: rgb(223, 219, 219) !important;
    }

    [data-testid="stSidebar"] select,
    [data-testid="stSidebar"] div[role="combobox"] {
        background-color: white !important;
        color: rgb(222, 217, 217) !important;
    }

    [data-testid="stSidebar"] .stSelectbox div,
    [data-testid="stSidebar"] .stSelectbox span {
        color: rgb(210, 204, 204) !important;
    }

/* Dropdown ke label text ka color */
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .css-1cpxqw2 {
    color: #efdbdb !important;
}

/* Optional: Button hover effects */
[data-testid="stSidebar"] button:hover {
    background-color: #e0e0e0 !important;
}

        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 18px;
            color: #2c2c54 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Title and description
st.markdown("<h1> 🚀Unit Converter using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write("✨Easily convert between different units of length, weight, and temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type:", ["Length", "Weight", "Temperature"])
value = st.sidebar.number_input("Enter Value:", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.sidebar.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Grams", "Kilograms", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Grams", "Kilograms", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_convertor(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Inches": 39.3701,
        "Feet": 3.28084
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value

# Button for conversion
if st.button("🔄Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_convertor(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'> Developed❤ by Musarrat Huma </div>", unsafe_allow_html=True)
