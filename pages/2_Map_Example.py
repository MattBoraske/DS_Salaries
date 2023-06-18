import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(
    page_title="Map Example",
    page_icon="🌎"
)

latitude = 40
longitude = -110

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [latitude, longitude],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=latitude,
        longitude=longitude,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))