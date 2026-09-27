
import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="SuperKart Sales Prediction",
    layout="wide"
)

st.title("SuperKart Sales Revenue Prediction")

st.write(
    "Predict product sales revenue using the trained Machine Learning model."
)

# Replace later with your deployed backend URL

BACKEND_URL = "http://backend:7860"

st.subheader("Single Prediction")

product_weight = st.number_input(
    "Product Weight",
    value=12.66
)

product_sugar_content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar","Regular","No Sugar"]
)

product_allocated_area = st.number_input(
    "Product Allocated Area",
    value=0.027
)

product_mrp = st.number_input(
    "Product MRP",
    value=117.08
)

store_size = st.selectbox(
    "Store Size",
    ["Small","Medium","High"]
)

store_city = st.selectbox(
    "Store Location City Type",
    ["Tier 1","Tier 2","Tier 3"]
)

store_type = st.selectbox(
    "Store Type",
    [
        "Departmental Store",
        "Food Mart",
        "Supermarket Type1",
        "Supermarket Type2"
    ]
)

product_id_char = st.selectbox(
    "Product ID Prefix",
    ["FD","NC","DR"]
)

store_age_years = st.number_input(
    "Store Age Years",
    value=16
)

product_type_category = st.selectbox(
    "Product Category",
    ["Perishables","Non Perishables"]
)

if st.button("Predict"):

    payload = {

        "Product_Weight": product_weight,

        "Product_Sugar_Content": product_sugar_content,

        "Product_Allocated_Area": product_allocated_area,

        "Product_MRP": product_mrp,

        "Store_Size": store_size,

        "Store_Location_City_Type": store_city,

        "Store_Type": store_type,

        "Product_Id_char": product_id_char,

        "Store_Age_Years": store_age_years,

        "Product_Type_Category": product_type_category
    }

    response = requests.post(
        f"{BACKEND_URL}/v1/predict",
        json=payload
    )

    st.success(
        f"Predicted Sales Revenue: {response.json()['Predicted_Sales'\]:.2f}"
    )
