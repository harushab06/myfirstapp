import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Header
st.header("Introduction to Streamlit")

# Subheader
st.subheader("A quick and easy way to create web apps in Python")

# Text
st.text("Streamlit is an open-source app framework for Machine Learning and Data Science projects. "
        "It allows you to create beautiful web applications with minimal effort. "
        "Below is a simple example of how you can display text using Streamlit.")

# Display a paragraph
paragraph = """
Environmental sustainability is a crucial aspect of modern development, emphasizing the need to balance human activities with the preservation of natural resources and ecosystems. 
It involves adopting practices that reduce waste, conserve energy, and minimize pollution, ensuring that future generations can meet their own needs without compromising the health of the planet. 
This holistic approach includes initiatives like renewable energy adoption, sustainable agriculture, and green building designs, which collectively contribute to a healthier, more resilient environment.
"""

st.write(paragraph)
