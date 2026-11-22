# 🌱 Plant Care Tracker App

## About the Project
Plant Care Tracker App is a simple plant care management application built with Python and Streamlit. It helps users manage their plants and keep track of their plant care activities.

## Features

- **Add Plants:** Add new plants with their name, location, date acquired, watering frequency, sunlight needs, and image.
- **Log Care:** Record care activities for selected plants and save their dates.
- **View Schedule:** View watering records and check which plants are due for watering.
- **Search Plants:** Search for plants by name or location and view their information and images.
- **Plant Statistics:** View statistics about saved plants and care activities.
- **File Management:** Upload CSV files, edit the uploaded data before importing, and download plant data as a CSV file.

## Technologies Used

- Python
- Streamlit
- Pandas
- CSV Files
- OS
- Datetime

## Installation

1. Clone or download the project.
2. Install the required libraries:

```bash
pip install streamlit pandas
```

3. Run the application:

```bash
streamlit run main.py
```

## Project Structure

```text
Plant Care Tracker App/
│
├── main.py
│
├── pages/
│   ├── add_plant.py
│   ├── files_management.py
│   ├── log_care.py
│   ├── plant_statistics.py
│   ├── search.py
│   └── view_schedule.py
│
├── data/
│   ├── plants.csv
│   └── care_log.csv
│
├── image/
│
└── README.md
```

## Data Storage

The application uses CSV files to store plant information and care activity records:

- `plants.csv`: Stores plant details.
- `care_log.csv`: Stores plant care activities and their dates.

## How to Use

1. Run the application using Streamlit.
2. Open the Add Plants page and enter the required plant information.
3. Go to Log Care to select a plant, choose a care activity, and record its date.
4. Visit View Schedule to check watering records and upcoming watering needs.
5. Use Search to find plants by name or location.
6. Visit Plant Statistics to view plant and care activity statistics.
7. Use File Management to upload, edit, import, or download CSV data.