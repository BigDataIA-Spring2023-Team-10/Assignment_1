import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import sqlite_main as db_methods

st.title('Locations of all NEXRAD sites')

sites_data = db_methods.get_nexrad_sites()

sites_data.head()

sitedf = pd.DataFrame(
    {
        "lat": sites_data['Latitude'],
        "lon": sites_data['Longitude']
    }
)

st.map(sitedf)
