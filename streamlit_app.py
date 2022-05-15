import streamlit as s
import pandas as p



mylist=p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

fruit_name=mylist.set_index('Fruit')

fruit_selected = s.multiselect("pick some fruits",list(fruit_name.index),['Banana','Apple'])
fruit_view=fruit_selected.loc[fruit_selected]
s.dataframe(fruit_view)
