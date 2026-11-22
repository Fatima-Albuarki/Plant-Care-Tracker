import streamlit as st
import pandas as pd
import os

# Title head
st.title("Search")
st.caption("Search plants by name or location")

# Read plants from session state 
plants = st.session_state["plants"]

# Search input 
search = st.text_input(
    "Enter plant name or location",
    placeholder="e.g. Rose"
)

# Search by plant name or location
if search:
    results = plants[
        plants["Plant Name"].str.contains(search, case=False, na=False) |
        plants["Location"].str.contains(search, case=False, na=False)
    ]
else:
    # Display all plants if search is empty
    results = plants

# Check if plant is not in the plant record "not found"
if results.empty:
    st.warning("No plants found. Try another name or location.")
    st.stop()

# Display number of plants found
st.write(f"Found {len(results)} plant(s)")

# Display all searched plant
for i in range(len(results)):

    # Create two columns one for image and one plant info
    col1, col2 = st.columns([1, 2])

    # AI assistance: Helped with displaying plant images and checking the image path before displaying them
    # Get plant image path
    image = results.iloc[i]["Image"]

    # Default image path
    DEFAULT_IMAGE = "image/defult.png"

    # Display image in the first column
    with col1:
        if not isinstance(image, str) or image == "":
            st.image(DEFAULT_IMAGE, width=150)

        elif os.path.exists(image):
            st.image(image, width=150)

        elif os.path.exists(os.path.join("image", image)):
            st.image(os.path.join("image", image), width=150)

        else:
            st.image(DEFAULT_IMAGE, width=150)

    # Display plant information in the second column
    with col2:
        # AI assistance: Helped with accessing and displaying plant information from each search result using iloc.
        st.subheader(results.iloc[i]["Plant Name"])
        st.write("Location:", results.iloc[i]["Location"])
        st.write("Date Acquired:", results.iloc[i]["Date Acquired"])
        st.write("Watering Frequency:", results.iloc[i]["Watering Frequency"], "days")
        st.write("Sunlight Needs:", results.iloc[i]["Sunlight Needs"])

    st.divider()