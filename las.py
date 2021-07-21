import streamlit as st
import lasio
import pandas as pd
archivo_las = lasio.read('LGAE-040.las')
df = archivo_las.df()
st.write(df)