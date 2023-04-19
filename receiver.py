import streamlit as st

def app():
    st.title("Receiver App")
    received_username = st.session_state.get("received_username", None)
    received_password = st.session_state.get("received_password", None)

    if received_username and received_password:
        st.subheader("Received Data:")
        st.write("Username:", received_username)
        st.write("Password:", received_password)

if __name__ == "__main__":
    app()
