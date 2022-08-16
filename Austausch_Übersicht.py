import pandas as pd
import streamlit as st

path_Input = r'C:/DATA/'

df = pd.read_excel(path_Input+'Austausch_Uebersicht_20220711.xlsx')


st.title('Austausch Übersicht')
