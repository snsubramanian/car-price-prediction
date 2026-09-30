import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)


# -----------------------------
# Load Model and Mapping
# -----------------------------

model = joblib.load("car_price_model.pkl")
car_map = joblib.load("car_name_map.pkl")


# -----------------------------
# Title
# -----------------------------

st.title("🚗 Car Price Prediction")

st.write(
    "Enter the car details below to predict the estimated car price."
)


# -----------------------------
# Input Section
# -----------------------------

st.header("Car Details")


# Car Name
car_name = st.selectbox(
    "Car Name",
    list(car_map.keys())
)


# Fuel Type
fueltype = st.selectbox(
    "Fuel Type",
    ["gas", "diesel"]
)


# Aspiration
aspiration = st.selectbox(
    "Aspiration",
    ["std", "turbo"]
)


# Door Number
doornumber = st.selectbox(
    "Number of Doors",
    ["two", "four"]
)


# Car Body
carbody = st.selectbox(
    "Car Body",
    [
        "convertible",
        "hatchback",
        "sedan",
        "wagon",
        "hardtop"
    ]
)


# Drive Wheel
drivewheel = st.selectbox(
    "Drive Wheel",
    [
        "fwd",
        "rwd",
        "4wd"
    ]
)


# Engine Location
enginelocation = st.selectbox(
    "Engine Location",
    [
        "front",
        "rear"
    ]
)


# Numerical Inputs

wheelbase = st.number_input(
    "Wheelbase",
    min_value=80.0,
    max_value=130.0,
    value=100.0
)

carlength = st.number_input(
    "Car Length",
    min_value=140.0,
    max_value=210.0,
    value=170.0
)

carwidth = st.number_input(
    "Car Width",
    min_value=60.0,
    max_value=75.0,
    value=65.0
)

carheight = st.number_input(
    "Car Height",
    min_value=45.0,
    max_value=60.0,
    value=54.0
)

curbweight = st.number_input(
    "Curb Weight",
    min_value=1300,
    max_value=4100,
    value=2500
)


# Engine Type
enginetype = st.selectbox(
    "Engine Type",
    [
        "dohc",
        "ohcv",
        "ohc",
        "l",
        "rotor",
        "ohcf",
        "dohcv"
    ]
)


# Number of Cylinders
cylindernumber = st.selectbox(
    "Number of Cylinders",
    [
        "two",
        "three",
        "four",
        "five",
        "six",
        "eight",
        "twelve"
    ]
)


enginesize = st.number_input(
    "Engine Size",
    min_value=50,
    max_value=350,
    value=120
)


# Fuel System
fuelsystem = st.selectbox(
    "Fuel System",
    [
        "mpfi",
        "2bbl",
        "idi",
        "1bbl",
        "spdi",
        "4bbl",
        "mfi",
        "spfi"
    ]
)


boreratio = st.number_input(
    "Bore Ratio",
    min_value=2.0,
    max_value=4.5,
    value=3.2
)


compressionratio = st.number_input(
    "Compression Ratio",
    min_value=7.0,
    max_value=25.0,
    value=9.0
)


horsepower = st.number_input(
    "Horsepower",
    min_value=40,
    max_value=300,
    value=100
)


peakrpm = st.number_input(
    "Peak RPM",
    min_value=4000,
    max_value=7000,
    value=5000
)


citympg = st.number_input(
    "City MPG",
    min_value=10,
    max_value=50,
    value=25
)


highwaympg = st.number_input(
    "Highway MPG",
    min_value=10,
    max_value=50,
    value=30
)


# -----------------------------
# Prediction Button
# -----------------------------

if st.button("Predict Car Price"):

    # Convert categorical values
    fueltype_value = {
        "gas": 0,
        "diesel": 1
    }[fueltype]

    aspiration_value = {
        "std": 0,
        "turbo": 1
    }[aspiration]

    doornumber_value = {
        "two": 2,
        "four": 4
    }[doornumber]

    carbody_value = {
        "convertible": 0,
        "hatchback": 1,
        "sedan": 2,
        "wagon": 3,
        "hardtop": 4
    }[carbody]

    drivewheel_value = {
        "fwd": 0,
        "rwd": 1,
        "4wd": 2
    }[drivewheel]

    enginelocation_value = {
        "front": 0,
        "rear": 1
    }[enginelocation]

    enginetype_value = {
        "dohc": 0,
        "ohcv": 1,
        "ohc": 2,
        "l": 3,
        "rotor": 4,
        "ohcf": 5,
        "dohcv": 6
    }[enginetype]

    cylindernumber_value = {
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "eight": 8,
        "twelve": 12
    }[cylindernumber]

    fuelsystem_value = {
        "mpfi": 0,
        "2bbl": 1,
        "idi": 2,
        "1bbl": 3,
        "spdi": 4,
        "4bbl": 5,
        "mfi": 6,
        "spfi": 7
    }[fuelsystem]

    # CarName mapping
    carname_value = car_map[car_name]


    # -----------------------------
    # Create Input DataFrame
    # -----------------------------

    input_data = pd.DataFrame([[
        carname_value,
        fueltype_value,
        aspiration_value,
        doornumber_value,
        carbody_value,
        drivewheel_value,
        enginelocation_value,
        wheelbase,
        carlength,
        carwidth,
        carheight,
        curbweight,
        enginetype_value,
        cylindernumber_value,
        enginesize,
        fuelsystem_value,
        boreratio,
        compressionratio,
        horsepower,
        peakrpm,
        citympg,
        highwaympg
    ]], columns=[
        "CarName",
        "fueltype",
        "aspiration",
        "doornumber",
        "carbody",
        "drivewheel",
        "enginelocation",
        "wheelbase",
        "carlength",
        "carwidth",
        "carheight",
        "curbweight",
        "enginetype",
        "cylindernumber",
        "enginesize",
        "fuelsystem",
        "boreratio",
        "compressionratio",
        "horsepower",
        "peakrpm",
        "citympg",
        "highwaympg"
    ])


    # -----------------------------
    # Prediction
    # -----------------------------

    prediction = model.predict(input_data)[0]


    # -----------------------------
    # Display Result
    # -----------------------------

    st.success(
        f"Estimated Car Price: ₹{prediction:,.2f}"
    )