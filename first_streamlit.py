import streamlit

streamlit.title('Ammar First App')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry')
streamlit.text('Khawsey')
streamlit.text('Mitthi ki BHaji')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), default=['Avocado', 'Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

fruits_to_show = my_fruit_list.loc[fruits_selected]

#selected_fruits = st.multiselect("Pick some fruits:", list(my_fruit_list.index), default=['Avocado', 'Strawberries'])
