import streamlit as st

def app():
    st.title("Receiver App")
    
    if st.request.method == "POST":
        username = st.request.form["username"]
        password = st.request.form["password"]
        st.session_state.received_username = username
        st.session_state.received_password = password
        st.write("Received Username:", username)
        st.write("Received Password:", password)
        
        # You can redirect the user to another page after receiving the data
        # using the `st.experimental_set_query_params` function.
        st.experimental_set_query_params(username=username, password=password)

    received_username = st.session_state.get("received_username", None)
    received_password = st.session_state.get("received_password", None)

    if received_username and received_password:
        st.subheader("Received Data:")
        st.write("Username:", received_username)
        st.write("Password:", received_password)

if __name__ == "__main__":
    app()
