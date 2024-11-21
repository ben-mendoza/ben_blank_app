import streamlit as st
import pandas as pd
import datetime

st.title("Hello! Welcome to Ben's App🎈")
st.write(
"Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write("Hi, what is your name?")
title = st.text_input("Name:")
st.write("Hello,", title, ". It is nice to have you here.")

today = datetime.datetime.now().date()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your your birthday",
    today,
    format="MM.DD.YYYY",
)

st.write("Your are:", today - d, "old.")

st.write(
"It seems this a different ... paragraph."
)

