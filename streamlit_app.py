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
streamlit.dataframe(my_fruit_list)
