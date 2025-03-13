import pandas as pd
import numpy as np
import streamlit as st

st.title('My first cloud app')

st.write(' A Simple DataFrame : ')

dF = pd.DataFrame(np.random.randn(10,2),columns=['Col1','Col2'])
st.dataframe(dF)

