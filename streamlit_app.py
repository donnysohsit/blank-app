import pandas as pd
import streamlit as st

import folium
import streamlit as st
from datetime import datetime
from streamlit_folium import st_folium

st.title("Anomaly Detection SG Mapper")

longlat_df = pd.read_csv("./data/LongLat.csv")
dim_df = pd.read_csv("./data/dim.csv")
linktable_df = pd.read_csv("./data/linktable.csv")

temp_location = (longlat_df["Location"])
selected_location = st.selectbox(
    "Choose your location.", temp_location
    )

temp_location = (longlat_df["Location"])
selected_row = longlat_df[longlat_df['Location'] == selected_location]
selected_long = selected_row['Latitude'].values
selected_lat = selected_row['Longitude'].values
selected_lkey = selected_row['LKey'].values.astype("str")

dim_df['RTUNumber'] = dim_df['RTUNumber'].astype("str")
linktable_df['Hkey'] = linktable_df['Hkey'].astype("str")

sensor_rows = dim_df[dim_df['RTUNumber'] == selected_lkey[0]]
options = sensor_rows['Equipment'].values

equip_dict = dim_df.set_index('Equipment')['RTUNumber'].to_dict()

# # Create the multi-select widget
selected_options = st.multiselect("Select the sensors:", options)
selected_values = [equip_dict.get(key, 'Key not found') for key in selected_options]

# # Display the selected options
st.write("You selected:", selected_values)

max_date = max(linktable_df["DateTime"])
min_date = min(linktable_df["DateTime"])

timestamp = datetime.strptime(max_date, "%Y-%m-%d %H:%M:%S.%f")
formatted_max_date = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
formatted_max_date = timestamp.date()

timestamp = datetime.strptime(min_date, "%Y-%m-%d %H:%M:%S.%f")
formatted_min_date = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
formatted_min_date = timestamp.date()

# # Create a date input widget
selected_date = st.date_input(
    "Select a date",
    value=formatted_max_date,  # Default to today's date
    min_value=formatted_min_date, # Minimum date
    max_value=formatted_max_date  # Maximum date
)
# # Display the selected date
st.write("You selected:", selected_date)

# hkey_list = linktable_df[linktable_df['Hkey'].isin(selected_options) & (linktable_df['DateTime'] == selected_date)]
hkey_list = linktable_df[linktable_df['Hkey'].isin(selected_values)]
st.write(hkey_list)

m = folium.Map(location=[selected_long, selected_lat], zoom_start=16)
folium.Marker(
    [selected_long, selected_lat],
    popup=selected_location,
    tooltip=selected_location
).add_to(m)
st_data = st_folium(m, width=725, height=200)