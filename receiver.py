import streamlit as st
import requests

def app():
    st.title("Receiver App")

    if st.button("Receive Data"):
        response = requests.post({"username": username, "password": password})
        if response.ok:
            received_data = response.json()
            st.subheader("Received Data:")
            st.write("Username:", received_data.get("username"))
            st.write("Password:", received_data.get("password"))
        else:
            st.write("Error:", response.status_code)

if __name__ == "__main__":
    app()
