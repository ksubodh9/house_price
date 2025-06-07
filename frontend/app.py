import streamlit as st
import requests

st.title("🏠 House Price Prediction App")

# Collect input from user
bedrooms = st.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Bathrooms", 1.0, 10.0, 2.5)
sqft_living = st.number_input("Sqft Living", 300, 10000, 2400)
floors = st.number_input("Floors", 1.0, 3.5, 2.0)
waterfront = st.selectbox("Waterfront View", [0, 1])
view = st.slider("View Rating", 0, 4, 2)
condition = st.slider("Condition", 1, 5, 3)
grade = st.slider("Grade", 1, 13, 7)
sqft_above = st.number_input("Sqft Above", 200, 10000, 2000)
sqft_basement = st.number_input("Sqft Basement", 0, 3000, 400)
yr_built = st.number_input("Year Built", 1900, 2023, 1995)
yr_renovated = st.number_input("Year Renovated", 0, 2023, 0)
lat = st.number_input("Latitude", 47.0, 49.0, 47.6062)
sqft_living15 = st.number_input("Sqft Living15", 300, 10000, 2500)

# API endpoint
api_url = "http://localhost:8000/ml/predict"

if st.button("Predict Price"):
    payload = {
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "sqft_living": sqft_living,
        "floors": floors,
        "waterfront": waterfront,
        "view": view,
        "condition": condition,
        "grade": grade,
        "sqft_above": sqft_above,
        "sqft_basement": sqft_basement,
        "yr_built": yr_built,
        "yr_renovated": yr_renovated,
        "lat": lat,
        "sqft_living15": sqft_living15
    }

    try:
        response = requests.post(api_url, json=payload)
        result = response.json()
        st.success(f"🏡 Predicted House Price: ${result['predicted_price']}")
    except Exception as e:
        st.error(f"Failed to get prediction. Error: {e}")
