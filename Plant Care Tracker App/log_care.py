
import streamlit as st
import pandas as pd

#Title head
st.title("Log Care")
st.caption("Select a plant, choose an activity and log the date.")

# care_log.csv file path
CARE_FILE = "data/care_log.csv"

# Read plant data from Session State
plants = st.session_state["plants"]

# Read care records
## If CARE_FILE doesnt exist, then create empty table
try:
    care_log = pd.read_csv(CARE_FILE)
except FileNotFoundError:
    care_log = pd.DataFrame(columns=[
        "Plant Name",
        "Activity",
        "Care Date"
    ])

# Check plants exsisting row
if len(plants) == 0:
    # If plant doesnt exsist then notify to add a plant first
    st.info("Please add a plant first.")

else:
    # If plant exsist then able to fill the input fields

    # Select plant
    plant = st.selectbox(
        "Select Plant",
        plants["Plant Name"]
    )

    # Select plant activity
    activity = st.selectbox(
        "Choose Activity",
        ["Watering", "Repotting", "Pruning", "Fertilizing"]
    )

    # Select care date
    care_date = st.date_input("Care Date")

    # Save record button
    if st.button("Save Care Record", type="primary"):

        #Create a new row
        new_row = pd.DataFrame({
            "Plant Name": [plant],
            "Activity": [activity],
            "Care Date": [str(care_date)]
        })

        # AI assistance: Helped with adding a new record to the existing care_log
        care_log.loc[len(care_log)] = [
            plant,
            activity,
            str(care_date)
        ]

        # Save care_log.csv & confirm successful saving
        care_log.to_csv(CARE_FILE, index=False)

        st.success("Care record saved!")
