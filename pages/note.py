from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import streamlit as st

# Access data
engine = create_engine('sqlite:///db/data.db', echo=True)
Base = declarative_base()

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a table
class NoteModel(Base):
    __tablename__ = 'notes'
    id = Column(String, primary_key=True, unique=True)
    title = Column(String)
    content = Column(String)
    category = Column(String)
    created_at = Column(String, default=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    updated_at = Column(String, default=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def __init__(self, title, content, category):
        self.title = title
        self.content = content
        self.category = category

    def __repr__(self):
        return f"<Note {self.title}>"

# Create table
Base.metadata.create_all(engine)

# Create a note
def create(title, content, category):
    note = NoteModel(title, content, category)
    session.add(note)
    session.commit()
    return note
def read_all():
    notes = session.query(NoteModel).all()
    return notes
def read_one(id):
    note = session.query(NoteModel).filter(NoteModel.id == id).first()
    return note
def update(id, title, content, category):
    note = session.query(NoteModel).filter(NoteModel.id == id).first()
    if title:
        note.title = title
    if content:
        note.content = content
    if category:
        note.category = category
    note.updated_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    session.commit()
    return note
def delete(id):
    note = session.query(NoteModel).filter(NoteModel.id == id).first()
    session.delete(note)
    session.commit()
    return note

# Create page interface
def create_page():
    st.title("Create Note")
    title = st.text_input("Title")
    content = st.text_area("Content")
    category = st.selectbox("Category", ["Personal", "Work"])
    if st.button("Create"):
        note = create(title, content, category)
        st.success(f"Created Note: {note.title}")
def read_all_page():
    st.title("View All Notes")
    notes = read_all()
    for note in notes:
        st.write(f"Title: {note.title}")
        st.write(f"Content: {note.content}")
        st.write(f"Category: {note.category}")
        st.write(f"Created At: {note.created_at}")
        st.write(f"Updated At: {note.updated_at}")
        st.write("---")
def read_one_page():
    st.title("View Note")
    id = st.text_input("ID",value="1")
    note = read_one(id)
    if note:
        st.write(f"Title: {note.title}")
        st.write(f"Content: {note.content}")
        st.write(f"Category: {note.category}")
        st.write(f"Created At: {note.created_at}")
        st.write(f"Updated At: {note.updated_at}")
def update_page():
    st.title("Update Note")
    id = st.number_input("ID")
    note = read_one(id)
    if note:
        title = st.text_input("Title", note.title)
        content = st.text_area("Content", note.content)
        category = st.selectbox("Category",["Personal", "Work"])
        if st.button("Update"):
            note = update(id, title, content, category)
            st.success(f"Updated Note: {note.title}")
def delete_page():
    st.title("Delete Note")
    id = st.number_input("ID")
    note = read_one(id)
    if note:
        if st.button("Delete"):
            note = delete(id)
            st.success(f"Deleted Note: {note.title}")
            
