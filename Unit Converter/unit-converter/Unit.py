import streamlit as st


st.set_page_config(
    page_title="Unit Converter",
    page_icon="📏",
    layout="centered"
)

# Custom CSS 
st.markdown("""
    <style>
    /* Custom Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Background Styling */
    .main {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }

    /* Header Styling */
    .stApp {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #007bff;
        color: white;
        padding: 0.8rem;
        border-radius: 10px;
        font-size: 16px;
        border: none;
        transition: 0.3s;
        width: 100%;
        font-weight: bold;
    }
    
    .stButton>button:hover {
        background-color: #0056b3;
        transform: scale(1.05);
    }

    /* Info & Success Box */
    .stAlert {
        border-radius: 10px;
        padding: 1rem;
        font-weight: bold;
    }
    
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: white;'>📏 Universal Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Easily convert between different units of measurement!</h4>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Conversion Categories & Factors
unit_categories = {
    "Length": {
        "meter": 1.0, "kilometer": 1000.0, "centimeter": 0.01,
        "millimeter": 0.001, "inch": 0.0254, "foot": 0.3048,
        "yard": 0.9144, "mile": 1609.344
    },
    "Mass": {
        "kilogram": 1.0, "gram": 0.001, "milligram": 0.000001,
        "pound": 0.453592, "ounce": 0.0283495
    },
    "Temperature": {
        "celsius": 1.0, "fahrenheit": 1.0, "kelvin": 1.0
    },
    "Volume": {
        "liter": 1.0, "milliliter": 0.001, "gallon": 3.78541,
        "quart": 0.946353, "pint": 0.473176, "cup": 0.236588, "fluid_ounce": 0.0295735
    },
    "Area": {
        "square_meter": 1.0, "square_kilometer": 1000000.0,
        "square_mile": 2589988.11, "square_yard": 0.836127,
        "square_foot": 0.092903, "acre": 4046.86
    },
    "Speed": {
        "meter_per_second": 1.0, "kilometer_per_hour": 0.277778, "mile_per_hour": 0.44704
    },
    "Time": {
        "second": 1.0, "minute": 60.0, "hour": 3600.0,
        "day": 86400.0, "week": 604800.0,
        "month": 2629746.0, "year": 31556952.0
    }
}

# Layout: Two Columns
col1, col2 = st.columns(2)

# Input Section
with col1:
    st.subheader("🔹 Input")
    category = st.selectbox("Select Category", list(unit_categories.keys()))
    input_value = st.number_input("Enter Value", min_value=0.0, value=1.0, format="%.2f")
    from_unit = st.selectbox("From Unit", list(unit_categories[category].keys()))

# Output Section
with col2:
    st.subheader("🔹 Output")
    to_unit = st.selectbox("To Unit", list(unit_categories[category].keys()))
    
    # Convert Button
    if st.button("Convert"):
        try:
            from_factor = unit_categories[category][from_unit]
            to_factor = unit_categories[category][to_unit]
            
          
            if category == "Temperature":
                if from_unit == "celsius" and to_unit == "fahrenheit":
                    result = (input_value * 9/5) + 32
                elif from_unit == "fahrenheit" and to_unit == "celsius":
                    result = (input_value - 32) * 5/9
                elif from_unit == "celsius" and to_unit == "kelvin":
                    result = input_value + 273.15
                elif from_unit == "kelvin" and to_unit == "celsius":
                    result = input_value - 273.15
                elif from_unit == "fahrenheit" and to_unit == "kelvin":
                    result = (input_value - 32) * 5/9 + 273.15
                elif from_unit == "kelvin" and to_unit == "fahrenheit":
                    result = (input_value - 273.15) * 9/5 + 32
                else:
                    result = input_value
            else:
                base_value = input_value * from_factor
                result = base_value / to_factor
            
            # Display Result
            st.success(f"✅ Result: {result:.4f} {to_unit}")
            st.info(f"📌 Formula: {input_value} {from_unit} = {result:.4f} {to_unit}")
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")


st.markdown("<hr>", unsafe_allow_html=True)

# **Tips & Instructions**
st.markdown("""
    ### 💡 How to Use:
    - Choose a **Category** (Length, Mass, Temperature, etc.)
    - Enter a **Value** and select **From & To Units**
    - Click **Convert** to get the result! 🎯
""", unsafe_allow_html=True)

# Credits
st.markdown("""
    <div style="text-align:center; padding-top:10px;">
        <p style="color:black; font-size: 16px;">💙 Made with Love by <b>Aamna Ansari</b></p>
    </div>
""", unsafe_allow_html=True)
