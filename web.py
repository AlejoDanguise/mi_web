import streamlit as st
import funciones

tareas = funciones.get_tarea()

def agregar_tarea():
    tarea = st.session_state["nueva_tarea"] + "\n"
    tareas.append(tarea)
    funciones.write_tarea(tareas)

st.title("Tareas Pendientes App")
st.subheader("Esta es mi app")
st.write("sdasdgsd")


for index,tarea in enumerate(tareas):
    checkbox = st.checkbox(tarea, key=tarea)
    if checkbox:
        tareas.pop(index)
        funciones.write_tarea(tareas)
        del st.session_state[tarea]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Ingresa un nueva tarea...",
              on_change=agregar_tarea, key="nueva_tarea")
