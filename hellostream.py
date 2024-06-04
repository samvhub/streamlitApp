# import streamlit as st

# # Display the text "Hello World!" on the web app
# st.write("Hello test!")
# st.write("Hello test!")


import streamlit as st

# Streamlit app title
st.title("Sample Code Presentation")

# Sample Python code
sample_code = """
def greet(name):
    return f"Hello, {name}!"

# Example usage
user_name = "John"
greeting = greet(user_name)
print(greeting)
"""

# Display the sample code
st.code(sample_code, language="python")

# Add a description
st.write("This is a simple Python function that greets a user by name.")

# Add a button
if st.button("Click me!"):
    st.write("Button clicked!")

# Add a slider
slider_value = st.slider("Select a value", min_value=0, max_value=10)
st.write(f"Selected value: {slider_value}")
