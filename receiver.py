import streamlit as st

# Define Streamlit app
def app():
    # Create a route to receive password data via POST request
    if st.request.method == "POST":
        password = st.request.form["password"]
        username = st.request.form["username"]
        st.write("Received Password:", password)
        st.write("Received Password:", username)

# Run Streamlit app
if __name__ == "__main__":
    app()
