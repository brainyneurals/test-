import streamlit as st

# Create a Streamlit sidebar to get user input
st.sidebar.header("User Input")

# Get user input for a text area
user_input_data = st.sidebar.text_area("Enter your data here:")

# Display the user input
st.write("User Input Data:")
st.write(user_input_data)
