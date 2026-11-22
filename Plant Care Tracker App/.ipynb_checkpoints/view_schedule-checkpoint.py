
import streamlit as st
import pandas as pd
import datetime

# Page title
st.title("View Schedule")
st.caption("View plants that are due for watering and check their watering status.")

# Read plant data from Session State
plants = st.session_state["plants"]

# Check if plants exist
if len(plants) == 0:
    st.info("Please add plants first.")
    st.stop()

# Read care records
try:
    care_log = pd.read_csv("data/care_log.csv")
except FileNotFoundError:
    st.info("No care records found. Please log plant care first.")
    st.stop()

# Create a separate DataFrame for the schedule
# AI assistance: Helped with resetting the DataFrame index to start from zero using reset_index(drop=True).
schedule = plants.copy().reset_index(drop=True)

# Create empty schedule columns
schedule["Last Watered"] = ""
schedule["Next Watering"] = ""
schedule["Status"] = ""

# Get today's date
today = datetime.date.today()

# Check each plant
for i in range(len(schedule)):

    # Get plant name and watering frequency
    # AI assistance: Helped with accessing and updating DataFrame values using .loc.
    plant_name = schedule.loc[i, "Plant Name"]
    frequency = schedule.loc[i, "Watering Frequency"]

    # Find watering records for this plant
    watering = care_log[
        (care_log["Plant Name"] == plant_name) &
        (care_log["Activity"] == "Watering")
    ]

    # Check if watering records exist
    if len(watering) > 0:

        # Get the latest watering date
        last_date = pd.to_datetime(watering["Care Date"]).max().date()

        # Calculate next watering date
        next_date = last_date + datetime.timedelta(days=int(frequency))

        # Check watering status
        if next_date < today:
            status = "Overdue"
            st.warning(f"{plant_name} is overdue for watering!", icon="⚠️")
        elif next_date == today:
            status = "Due Today"
            st.warning(f"{plant_name} needs watering today!", icon="⚠️")
        else:
            status = "Upcoming"

        # Save schedule information
        schedule.loc[i, "Last Watered"] = str(last_date)
        schedule.loc[i, "Next Watering"] = str(next_date)
        schedule.loc[i, "Status"] = status

# AI assistance: Helped with filtering plants that have watering records using the Last Watered column.
# Filter plants that have watering records
watering_plants = schedule[schedule["Last Watered"] != ""]

# Schedule title
st.subheader("Watering Schedule")

# Check if watering records exist
if len(watering_plants) > 0:

    # Display watering schedule
    # AI assistance: Helped with using hide_index and use_container_width to adjust the table display.
    st.dataframe(
        watering_plants[["Plant Name", "Last Watered", "Next Watering", "Status"]],
        hide_index=True,
        use_container_width=True
    )

else:
    st.info("No watering records found. Please log watering activities.")
