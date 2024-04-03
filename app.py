import streamlit as st
import altair as alt

alt.themes.enable("dark")

st.set_page_config(page_title='godega.io',
                #    page_icon='assets/Nevil.png',
                   layout='wide'
)

st.markdown("<center>Coming Soon!</center>", unsafe_allow_html=True)
st.write("#")
st.write("#")
st.markdown("<center><h1>godega.io</h1></center>", unsafe_allow_html=True)
st.caption("<center>On-Premise Snack Sets<br>SIMPLIFIED</center>", unsafe_allow_html=True)
st.write("#")
st.write("#")
st.write("#")
st.markdown("<center><h5>Travel  |  Convenience  |  Specialty Retail  |  Office  |  Campus  |  Hospitality  |  Healthcare</center>", unsafe_allow_html=True)

st.write("#")
st.write("#")
st.write("#")
st.write("#")


col1, col2, col3, col4, col5, col6, col7= st.columns(7)
with col1:
    st.image(r"awake2.jpg",width=100)
with col2:
    st.image(r"wilde1.jpg",width=100)
with col3:
    st.image(r"kind.jpeg",width=100)
with col4:
    st.image(r"chocoloney3.jpg",width=100)
with col5:
    st.image(r"lara.jpg",width=75)
with col6:
    st.image(r"popcorners.jpg",width=100)
with col7:
    st.image(r"grillos.png",width=100)