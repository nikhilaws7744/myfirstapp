import streamlit as s
import pandas as p

mylist=p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
s.dataframe(mylist)
