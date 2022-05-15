import streamlit as s
import pandas as p



mylist=p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

fruit_name=list(mylist.index)

s.multiselect("pick some fruits",list(mylist.fruit_name))
s.dataframe(mylist)
