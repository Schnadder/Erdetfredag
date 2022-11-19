from datetime import date
import streamlit as st

st.set_page_config()
leftCol, mainCol = st.columns([1,3])
with mainCol:
    st.title("Er det fredag?")

today = date.today()

if today.strftime("%A") == "Friday":
    with mainCol:
        st.subheader("JA!")
else:
    with mainCol:
        st.subheader("Nei :(")