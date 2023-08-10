import streamlit

streamlit.title('Ammar First App')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry')
streamlit.text('Khawsey')
streamlit.text('Mitthi ki BHaji')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
