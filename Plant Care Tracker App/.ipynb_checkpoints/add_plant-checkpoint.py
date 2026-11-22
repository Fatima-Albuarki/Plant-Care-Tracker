
import datetime
import pandas as pd
import streamlit as st
import os


# Title head
st.title("Add New Plant")
st.caption("Enter your plant details and upload a picture.")

# Text input to captures plant name
name = st.text_input("Plant Name")

# Text input to captures plant location
location = st.text_input("Location")

# Date input to captures plant date acquired
acquired = st.date_input(
    "Date Acquired",
    value=datetime.date.today()
)

# Number input to captures plant watering frequency (days)
days = st.number_input(
    "Watering Frequency (days)",
    min_value=1,
    value=1
)

# Select box to captures plant sunlight needs
sunlight = st.selectbox(
    "Sunlight Needs",
    ["Full sun", "Partial sun", "Shade"]
)

# Upload photo of user's plant with .jpg and .png format
# Note: The uploaded photo will display in search page
image = st.file_uploader(
    "Upload Plant Image",
    type=["jpg", "png"]
)

# The button checks the input fields if they fully meet the conditions
# If not, the user will be notified by an error
if st.button("Save Plant", type="primary"):

    if name.strip() == "":
        st.error("Please enter a plant name.")

    elif image is None:
        st.error("Please upload a plant image.")

    else:
        # AI assistance: Helped with saving the uploaded image
        #Save uploaded photo in image folder
        os.makedirs("image", exist_ok=True)
        image_path = "image/" + image.name

        with open(image_path, "wb") as file:
            file.write(image.getbuffer())

        # Create new plant row
        new_row = pd.DataFrame({
            "Plant Name": [name.strip()],
            "Location": [location.strip()],
            "Date Acquired": [str(acquired)],
            "Watering Frequency": [days],
            "Sunlight Needs": [sunlight],
            "Image": [image_path]
        })

        # AI assistance: Helped with combining existing plant data using .concat
        # Add new plant data to the plant session state
        plants = pd.concat(
            [st.session_state["plants"], new_row],
            ignore_index=True
        )

        st.session_state["plants"] = plants

        # Save plants.csv & confirm successful saving
        plants.to_csv("data/plants.csv", index=False)

        st.success("Plant added successfully!")
