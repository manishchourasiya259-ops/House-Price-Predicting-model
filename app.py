import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("House price Prediction Model.pkl")

st.title("🏠 House Price Predictor")
st.write("Enter the house details below to predict its price.")

# Default values — user can change them
gr_liv_area = st.number_input("Living Area (sq ft)", min_value=0, value=1500)
lot_area = st.number_input("Lot Area (sq ft)", min_value=0, value=8000)
bedroom_abv_gr = st.number_input("Bedrooms", min_value=0, value=3)
full_bath = st.number_input("Full Bathrooms", min_value=0, value=2)

overall_qual = st.slider("Overall Quality", 1, 10, 5)
overall_cond = st.slider("Overall Condition", 1, 10, 5)

year_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=2000)
year_remod = st.number_input("Year Remodeled", min_value=1800, max_value=2026, value=2000)

total_bsmt_sf = st.number_input("Basement Area (sq ft)", min_value=0, value=800)
garage_cars = st.number_input("Garage Capacity (cars)", min_value=0, value=2)

central_air = st.selectbox("Central Air", ["Y", "N"], index=0)

pool_area = st.number_input("Pool Area (sq ft)", min_value=0, value=0)
fireplaces = st.number_input("Fireplaces", min_value=0, value=0)

wood_deck_sf = st.number_input("Wood Deck Area (sq ft)", min_value=0, value=0)
open_porch_sf = st.number_input("Open Porch Area (sq ft)", min_value=0, value=0)
enclosed_porch = st.number_input("Enclosed Porch Area (sq ft)", min_value=0, value=0)

neighborhood = st.text_input("Neighborhood", value="NAmes")


# Predict
if st.button("Predict House Price"):

    new_house = pd.DataFrame([{
        "Gr Liv Area": gr_liv_area,
        "Lot Area": lot_area,
        "Bedroom AbvGr": bedroom_abv_gr,
        "Full Bath": full_bath,
        "Overall Qual": overall_qual,
        "Overall Cond": overall_cond,
        "Year Built": year_built,
        "Year Remod/Add": year_remod,
        "Total Bsmt SF": total_bsmt_sf,
        "Garage Cars": garage_cars,
        "Central Air": central_air,
        "Pool Area": pool_area,
        "Fireplaces": fireplaces,
        "Wood Deck SF": wood_deck_sf,
        "Open Porch SF": open_porch_sf,
        "Enclosed Porch": enclosed_porch,
        "Neighborhood": neighborhood
    }])

    prediction = model.predict(new_house)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")