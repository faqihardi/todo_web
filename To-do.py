import streamlit as st
import functions

st.set_page_config(layout="wide")

st.title("My To-do App")
st.subheader("Welcome to To-do List App")
st.text("This App make your life easier")

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_to_do"] + "\n"
    todos.append(todo)
    functions.writes_todos(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writes_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_to_do")

