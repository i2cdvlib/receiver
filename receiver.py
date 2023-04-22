import streamlit as st
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("0.0.0.0", 9000))

st.subheader("received message")


while True :
    st.write(client.recv(2000).decode('utf-8'))
