import streamlit as st
from streamlit_option_menu import option_menu
import BrandAnalysis as ba
import Visualization as v
import os
os.chdir("P:\\PyCharm Selenium Practice\\pythonProject\\Sentiment Analysis\\Final Project")

st.title("Sentimental Analysis")
selected = option_menu(
        menu_title=None,
        options=["Home", "Account", "Brand Analysis", "Visualization"],
        icons=['house','person-circle','graph-up-arrow','pie-chart'],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Account":
    st.title(f"You have selected {selected}")
if selected == "Brand Analysis":
    ba.brand_analysis()
if selected == "Visualization":
    v.visual()
