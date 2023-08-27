
from note import create_page, read_all_page, update_page, delete_page
import streamlit as st

# Create multiple pages with page state
PAGES = {
    "Create": create_page,
    "Read All": read_all_page,
    # "Read One": read_one_page,
    "Update": update_page,
    "Delete": delete_page
}

# Create page selector
st.sidebar.title("Menu")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

# Run the selected page
page()