import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name :") ##it will initially show a text box nd when we press enter the value will get stored in name
if name:
    st.write(f"Hello {name}")

age=st.slider("Select ur age :",0,100,25) ##25 is automatically selected at the start
st.write(f"Your age is {age}")

option=["Python", "Java", "C++", "JavaScript"]
choice=st.selectbox("Choose your Favourite Language :", option)
st.write(f"You Selected {choice}")

data = {
    'name':['Suraj','John','Krish','Jake'],
    'Age':[22,25,30,29],
    'City':['Bangalore','NewYork','FLorida', "Chicago"]
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file=st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)