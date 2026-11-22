
import streamlit as st
import pandas as pd

#---Initialize database---

# plants.csv file path
PLANTS_FILE = "data/plants.csv"

# Plant required columns
required_columns = [
    "Plant Name",
    "Location",
    "Date Acquired",
    "Watering Frequency",
    "Sunlight Needs",
    "Image"
]

# Save required columns in Session State
st.session_state["required_columns"] = required_columns

# Applying session state to hold plant data during the session
if "plants" not in st.session_state:
    try:
        st.session_state["plants"] = pd.read_csv(PLANTS_FILE)
    except FileNotFoundError:
        st.session_state["plants"] = pd.DataFrame(columns=required_columns)


#---Navigation Menu---

# Nav pages
pages = [
    st.Page("add_plant.py", title="Add Plant", icon=":material/add_circle:"),
    st.Page("log_care.py", title="Log Care", icon=":material/water_drop:"),
    st.Page("view_schedule.py", title="View Schedule", icon=":material/calendar_month:"),
    st.Page("search.py", title="Search Plant", icon=":material/search:"),
    st.Page("plant_statistics.py", title="Plant Statistics", icon=":material/bar_chart:"),
    st.Page("files_management.py", title="Files Management", icon=":material/folder:")
]

pg = st.navigation(pages, position="hidden")

with st.sidebar:
    st.title("🌱 Plant Care Tracker")

    # AI assistance: Helped with using a for loop to display
    # all page titles in the sidebar instead of placing them under the default navigation menu.
    for p in pages:
        st.page_link(p)

# Clear plants data
#pd.read_csv("data/plants.csv").iloc[0:0].to_csv("data/plants.csv", index=False)

# Clear care records
#pd.read_csv("data/care_log.csv").iloc[0:0].to_csv("data/care_log.csv", index=False)

pg.run()
