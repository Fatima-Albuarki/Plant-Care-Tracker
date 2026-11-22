
import streamlit as st
import pandas as pd

# Page title
st.title("Plant Statistics")
st.caption("View statistics about your plants and care activities.")

# Read plant data
plants = st.session_state["plants"]

try:
    # Read care records
    care_log = pd.read_csv("data/care_log.csv")

    # Check if care records exist, if not a notification will apear to indecat that no data yet to display
    if len(care_log) == 0:
        st.info("No care records available yet.")

    else:
        # var for calculate total plants and activities
        total_plants = len(plants)
        total_activities = len(care_log)

        # var for count each care activity
        activity_counts = care_log["Activity"].value_counts()

        # Var for get the most common activity
        most_common = activity_counts.index[0]

        # Display plant overview result
        st.subheader("Overview")

        # AI assistance: Helped with organizing the statistics into three columns using st.columns()
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Plants", total_plants)

        with col2:
            st.metric("Total Care Activities", total_activities)

        with col3:
            st.metric("Most Common Activity", most_common)

        # Activity statistics
        st.divider()
        st.subheader("Care Activity Statistics")

        st.bar_chart(activity_counts, color="#4CAF50")

except FileNotFoundError:
    st.info("No care records found. Please log some plant care activities.")
