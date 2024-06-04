# import streamlit as st

# # Display the text "Hello World!" on the web app
# st.write("Hello test!")
# st.write("Hello test!")


# import streamlit as st

# # Streamlit app title
# st.title("Sample Code Presentation")

# # Sample Python code
# sample_code = """
# def greet(name):
#     return f"Hello, {name}!"

# # Example usage
# user_name = "John"
# greeting = greet(user_name)
# print(greeting)
# """

# # Display the sample code
# st.code(sample_code, language="python")

# # Add a description
# st.write("This is a simple Python function that greets a user by name.")

# # Add a button
# if st.button("Click me!"):
#     st.write("Button clicked!")

# # Add a slider
# slider_value = st.slider("Select a value", min_value=0, max_value=10)
# st.write(f"Selected value: {slider_value}")
#-----------------------------#
#-----------------------------#
#-----------------------------#
import streamlit as st
import requests
import streamlit as st
import pandas as pd

def load_data(data_source):
    # Load data from the specified data source (e.g., URL or local file)
    try:
        data = pd.read_json(data_source)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def main():
    st.title("Data Loader App")

    # Text input for data source (URL or local file path)
    data_source = st.text_input("Enter data source (URL or file path):")

    # Button to load data
    if st.button("Load Data"):
        if data_source:
            loaded_data = load_data(data_source)
            if loaded_data is not None:
                st.success("Data loaded successfully!")
                st.write(loaded_data.head())
        else:
            st.warning("Please enter a valid data source.")

if __name__ == "__main__":
    main()
