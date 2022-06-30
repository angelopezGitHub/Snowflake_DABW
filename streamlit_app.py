import streamlit
import pandas

streamlit.title('My Parents New Healty Diner')
streamlit.header('This is how it starts with streamlit/python/snowflake')

streamlit.subheader('Menu')
streamlit.text('🦈 Tuna Sandwich')
streamlit.text('🐔 chicken breast Sandwich')
streamlit.text('🦈🥗Tuna Salad')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocato Toast')

#new tittle
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#getting file from site and show it
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
my_fruit_list = my_fruit_list.set_columns('Fruit','Serving_Size','Calories')

#add selection into a variable and then lets use that
fruits_selected = streamlit.multiselect("Select some fruits: ", list(my_fruit_list.index),['Apple','Banana','Kiwifruit','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

#show as a list, only mentioned columns
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
