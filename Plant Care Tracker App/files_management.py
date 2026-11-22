
import streamlit as st
import pandas as pd
import os

# CSV file path
PLANTS_FILE = "data/plants.csv"
CARE_FILE = "data/care_log.csv"

# Create data folder if it does not exist
os.makedirs("data", exist_ok=True)

# Plant required columns
required_columns = st.session_state["required_columns"]

# Page title
st.title("File Management")
st.caption("Manage CSV files (Download / Upload).")

# Upload CSV
uploaded_file = st.file_uploader("Upload plant CSV", type="csv")

if uploaded_file is not None:

    # Read uploaded file
    new_plants = pd.read_csv(uploaded_file)

    # AI assistance: Helped with checking whether the uploaded CSV
    # contains all the required columns
    columns_match = True

    for col in required_columns:
        if col not in new_plants.columns:
            columns_match = False

    if columns_match:

        # Keep only required columns
        new_plants = new_plants[required_columns]

        # Allow user to edit uploaded plants
        edited_plants = st.data_editor(
            new_plants,
            use_container_width=True
        )

        if st.button("Import CSV"):

            # AI assistance: Helped with combining existing plant data with uploaded plant data using pd.concat()
            plants = pd.concat(
                [st.session_state["plants"], edited_plants],
                ignore_index=True
            )

            # Remove duplicate plant records
            plants = plants.drop_duplicates()

            # Update session state
            st.session_state["plants"] = plants

            # Save updated CSV
            plants.to_csv(PLANTS_FILE, index=False)
            st.success("Plants imported successfully!")

    else:
        st.error("Please upload a CSV file with the correct columns.")


# Download Plant CSV
plants = st.session_state["plants"]

st.write("Download Plant CSV")

st.download_button(
    "Download",
    data=plants.to_csv(index=False),
    file_name="plants.csv",
    mime="text/csv"
)
