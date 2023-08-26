from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pages.note import NoteModel, create_page, read_all_page, read_one_page, update_page, delete_page
import streamlit as st

# Access data
engine = create_engine('sqlite:///db/data.db', echo=True)
Base = declarative_base()

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Show entire table data and have option for update or delete on each row
def read_all_page():
    st.title("Read All Notes")
    notes = session.query(NoteModel).all()
    for note in notes:
        st.write(f"{note.id} | {note.title} | {note.content} | {note.category} | {note.created_at} | {note.updated_at}")
        if st.button(f"Update {note.id}"):
            update_page()
        if st.button(f"Delete {note.id}"):
            delete_page()

if __name__ == "__main__":
    read_all_page()