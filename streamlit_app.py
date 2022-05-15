import streamlit as s
import pandas as p



mylist=p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_list=mylist.set_index('Fruit')

fruit_selected = s.multiselect("pick some fruits",list(my_list.index),['Banana','Apple'])
fruit_view=my_list.loc[fruit_selected]
s.dataframe(fruit_view)
