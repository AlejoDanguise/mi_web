
def get_tarea(filepath="tareas.txt"):
    with open(filepath, "r") as file:
        tareas = file.readlines()
    return tareas

def write_tarea(tareas_arg, filepath="tareas.txt"):
    with open(filepath, "w") as file:
        file.writelines(tareas_arg)