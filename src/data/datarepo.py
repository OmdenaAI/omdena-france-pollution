import streamlit as st
import os 
from glob import glob
import pandas as pd 
import matplotlib.pyplot as plt

st.header("View csv file from data folder")
csv_files = glob("**/*.csv", recursive = True)
selected_csv_file = st.selectbox("select a csv file", csv_files)

st.text("Selected file path: %s" %(os.path.join(os.getcwd(), selected_csv_file)))

selected_df = pd.read_csv(selected_csv_file)

st.write
st.write(selected_df)

# st.header("Visualize the data")

# col1, col2 = st.beta_columns(2)
# print(selected_df.columns.to_list())
# X = col1.selectbox("select column for x", [(index,column) for index,column in enumerate(selected_df.columns.to_list())])
# Y = col2.selectbox("select column for y", [(index,column) for index,column in enumerate(selected_df.columns.to_list())])
# index_start = st.number_input("Starting index, (0 to {})".format(len(selected_df)-1), min_value = 0, max_value = len(selected_df)-1)

# plt.plot(selected_df.iloc[index_start:, X[0]], selected_df.iloc[index_start:,Y[0]])
# st.pyplot(plt)
         